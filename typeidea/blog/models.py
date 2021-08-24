from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(verbose_name='名称', max_length=50)
    status = models.PositiveIntegerField(
        verbose_name='状态', default=STATUS_NORMAL, choices=STATUS_ITEMS)
    is_nav = models.BooleanField(verbose_name='是否为导航', default=False)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=10, verbose_name='名称')
    status = models.PositiveIntegerField(
        default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    desc = models.CharField(max_length=1024, blank=True, verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文需为MarkDown格式')
    status = models.PositiveIntegerField(
        default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']
