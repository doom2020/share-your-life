from django.db import models

# Create your models here.


class UserInfo(models.Model):
    name = models.CharField(verbose_name='昵称', max_length=50)
    phone = models.CharField(verbose_name='手机号', max_length=10, blank=True, null=True)
    email = models.EmailField(verbose_name='邮箱', max_length=50, blank=True, null=True)
    gender = models.CharField(verbose_name='性别', max_length=10, blank=True, null=True)
    face_info = models.CharField(verbose_name='人脸特征', max_length=10000, blank=True, null=True)
    picture = models.CharField(verbose_name='头像', max_length=100, blank=True, null=True)
    password = models.CharField(verbose_name='密码', max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')
    is_delete = models.BooleanField(verbose_name='是否禁用', default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_info'


class Classify(models.Model):
    name = models.CharField(verbose_name='类型名称', max_length=50)
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')
    comment = models.CharField(verbose_name='备注', max_length=100, blank=True, null=True)
    is_delete = models.BooleanField(verbose_name='是否删除', default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'classify'


class Article(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50)
    picture = models.CharField(verbose_name='图片', max_length=100, blank=True, null=True)
    content = models.TextField(verbose_name='文章内容', blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')
    is_delete = models.BooleanField(verbose_name='是否删除', default=0)
    user_info = models.ForeignKey(UserInfo, on_delete=True, verbose_name='作者')
    classify = models.ForeignKey(Classify, on_delete=True, verbose_name='文章类型')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'article'


class CommentInfo(models.Model):
    content = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')
    is_delete = models.BooleanField(verbose_name='是否删除', default=0)
    user_info = models.ForeignKey(UserInfo, on_delete=True, verbose_name='评论人')
    article = models.ForeignKey(Article, on_delete=True, verbose_name='评论文章')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'comment_info'


class SysMenu(models.Model):
    name = models.CharField(verbose_name='菜单名', max_length=50)
    parent_menu = models.CharField(verbose_name='父菜单', max_length=50)
    comment = models.CharField(verbose_name='备注', max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')
    is_delete = models.BooleanField(verbose_name='是否删除', default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'sys_menu'


class Rule(models.Model):
    name = models.CharField(verbose_name='角色名', max_length=50)
    permission = models.CharField(verbose_name='权限', max_length=100)
    comment = models.CharField(verbose_name='备注', max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')
    is_delete = models.BooleanField(verbose_name='是否删除', default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'rule'


class RuleUser(models.Model):
    account = models.CharField(verbose_name='用户', max_length=50)
    comment = models.CharField(verbose_name='备注', max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')
    is_delete = models.BooleanField(verbose_name='是否删除', default=0)
    rule = models.ForeignKey(Rule, on_delete=True)

    def __str__(self):
        return self.account

    class Meta:
        db_table = 'rule_user'


class Permission(models.Model):
    name = models.CharField(verbose_name='权限名', max_length=50)
    type = models.CharField(verbose_name='权限类型', max_length=50)
    comment = models.CharField(verbose_name='备注', max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间')
    update_time = models.DateTimeField(verbose_name='更新时间')
    is_delete = models.BooleanField(verbose_name='是否删除', default=0)
    sys_menu = models.ForeignKey(SysMenu, on_delete=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'permission'


class Proxy(models.Model):
    ip = models.CharField(verbose_name='ip地址', max_length=50)
    port = models.CharField(verbose_name='端口', max_length=10)
    anonymous = models.CharField(verbose_name='匿名度', max_length=10)
    type = models.CharField(verbose_name='类型', max_length=10)
    location = models.CharField(verbose_name='位置', max_length=30)
    response_speed = models.CharField(verbose_name='响应速度', max_length=20)
    last_validation_time = models.DateTimeField(verbose_name='最后验证时间')
    score = models.IntegerField(verbose_name='分数', default=100)
    is_delete = models.BooleanField(verbose_name='是否删除', default=0)

    def __str__(self):
        return self.ip

    class Meta:
        db_table = 'proxy'







