from punns.models import Punn
from punns.models import Tags
from accounts.models import UserProfile
from comments.models import Comment
from images.models import Image
from votes.models import CommentVote, PunnVote
from django.contrib import admin

admin.site.register(Punn)
admin.site.register(Tags)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(CommentVote)
admin.site.register(PunnVote)
admin.site.register(Image)


