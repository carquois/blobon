from punns.models import Punn
from accounts.models import UserProfile
from comments.models import Comment
from images.models import Image
from django.contrib import admin

admin.site.register(Punn)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Image)


