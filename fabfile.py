import os
from datetime import datetime

from jinja2 import Environment, FileSystemLoader, select_autoescape
from fabric.tasks import task

PROJECT_NAME = 'typeidea'
SETTINGS_BASE = 'typeidea/typeidea/settings/base.py'
DEPLOY_PATH = '/home/sanlo/venvs/typeidea-env'
VENV_ACTIVATE = os.path.join(DEPLOY_PATH, 'bin', 'activate')
PYPI_HOST = '127.0.0.1'
PYPI_INDEX = 'http://127.0.0.1:18080/simple'
PROCESS_COUNT = 2
PORT_PREFIX = 909


@task
def hello(c):
    result = c.run('echo $SHELL')
    user_shell = result.stdout.strip('\n')
    c.put('./tmp/supervisord.conf', '/home/sanlo/supervisord.conf')


@task
def build(c, version=None, bytescode=False):
    ''' build TYPEIDEA package

    Usage: fab -H centos --prompt-for-login-password build --version 0.2
    '''
    if not version:
        version = datetime().now().strftime('%m%d%H%M%S')

    _version = _Version()
    _version.set(['setup.py', SETTINGS_BASE], version)

    result = c.run('echo $SHELL', hide=True)
    user_shell = result.stdout.strip('\n')
    _ensure_virtualenv(c)
    c.local('python setup.py bdist_wheel upload -r centos', replace_env=False)

    _version.revert()


@task
def deploy(c, version, profile='develop'):
    ''' remote deploy to centos server
    部署指定版本
        1. 确认虚拟环境已经配置
        2. 激活虚拟环境
        3. 安装软件包
        4. 启动
        Usage:
            fab -H centos --prompt-for-login-password deploy --version 0.2 --profile develop
    '''
    _ensure_virtualenv(c)
    package_name = PROJECT_NAME + '==' + version
    with c.prefix('cd %s' % DEPLOY_PATH):
        c.run('pipenv run pip install %s -i %s --trusted-host %s' % (
            package_name,
            PYPI_INDEX,
            PYPI_HOST,
        ))
        _reload_supervisoird(c, DEPLOY_PATH, profile)


class _Version:
    origin_record = {}

    def replace(self, f, version):
        with open(f, 'r') as fd:
            origin_record = fd.read()
            content = origin_record.replace('${version}', version)

        with open(f, 'w') as fd:
            fd.write(content)

        self.origin_record[f] = origin_record

    def set(self, file_list, version):
        for f in file_list:
            self.replace(f, version)

    def revert(self):
        for f, content in self.origin_record.items():
            with open(f, 'w') as fd:
                fd.write(content)


def _ensure_virtualenv(c):
    if c.run('test -f %s/Pipfile' % DEPLOY_PATH, warn=True).ok:
        return True

    if c.run('test -d %s' % DEPLOY_PATH, warn=True).failed:
        c.run('mkdir -p %s' % DEPLOY_PATH)

    with c.prefix('cd %s' % DEPLOY_PATH):
        c.run('pipenv install django')
    c.run('mkdir -p %s/tmp' % DEPLOY_PATH)


def _upload_conf(c, deploy_path, profile):
    env = Environment(
        loader=FileSystemLoader('conf'),
        autoescape=select_autoescape(['.conf'])
    )
    template = env.get_template('supervisord.conf')
    context = {
        'process_count': PROCESS_COUNT,
        'port_prefix': PORT_PREFIX,
        'profile': profile,
        'deploy_path': deploy_path,
    }
    content = template.render(**context)
    tmp_file = './tmp/supervisord.conf'
    with open(tmp_file, 'wb') as f:
        f.write(content.encode('utf-8'))

    destination = os.path.join(deploy_path, 'supervisord.conf')
    print(destination)
    # c.put(tmp_file, destination)
    c.put(tmp_file, '/home/sanlo/venvs/typeidea-env/supervisord.conf')


def _reload_supervisoird(c, deploy_path, profile):
    _upload_conf(c, deploy_path, profile)
    with c.prefix('cd %s' % DEPLOY_PATH):
        print('====================CTL START==================================')
        c.run('pipenv run supervisorctl -c supervisord.conf shutdown', warn=True)
        print('====================CTL END==================================')
        c.run('pipenv run supervisorctl -c supervisord.conf start all')
