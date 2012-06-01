from punns.models import Punn
from accounts.models import UserProfile
from comments.models import Comment
from django.contrib import admin

admin.site.register(Punn)
admin.site.register(UserProfile)
admin.site.register(Comment)

