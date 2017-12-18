from django.contrib import admin
from . import models
# Register your models here.


# thanks to that we can see members of perticular group
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
