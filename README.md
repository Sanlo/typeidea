# Useful Linux Commnad

## Firewall
### Opening port
1. Get a list of allowed ports in the current zone:
> firewall-cmd --list-ports
2. Add a port to the allowed ports to open it for incoming traffic:
> sudo firewall-cmd --add-port=port-number/port-type[TCP/UDP]
3. Remove the port from the allowed ports to close it for the incoming traffic:
> sudo firewall-cmd --remove-port=port-number/port-type
4. Make the new settings persistent:
> sudo firewall-cmd --runtime-to-permanent


## File copy

Copy from **server** to **local**. Need to get private SSH key from server first.

Sytex:

> scp [-1246BCpqrv] [-c cipher] [-F ssh_config] [-i identity_file]
[-l limit] [-o ssh_option] [-P port] [-S program]
[[user@]host1:]file1 [...] [[user@]host2:]file2

Example:
>  scp sanlo@192.168.0.150:/home/sanlo/venvs/typeidea-env/conf/supervisord.conf .\Documents\Python\typeidea\conf\supervisord.conf


# Auto deployment
## Gunicorn
If used to run Python Web wsgi. Must run following cmd in the same path of **manage.py**
> gunicorn typyidea.wsgi:application -w 1 -b 0.0.0.0:8000

## Supervisor

### Create template
> echo_supervisord_conf >> conf/supervisord.conf

### Start project
> supervisord -c conf/supervisord.conf
