from punn.models import Punn
from account.models import UserProfile
from comment.models import Comment
from django.contrib import admin

admin.site.register(Punn)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Tag)

