from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserInfo)
admin.site.register(Classify)
admin.site.register(Article)
admin.site.register(CommentInfo)
admin.site.register(SysMenu)
admin.site.register(Rule)
admin.site.register(RuleUser)
admin.site.register(Permission)
