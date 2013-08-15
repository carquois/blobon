from punns.models import Punn
from punns.models import Favorite 
from punns.models import Tags
from punns.models import Reblog
from accounts.models import UserProfile
from comments.models import Comment
from images.models import Image
from votes.models import CommentVote, PunnVote
from news.models import Post
from django.contrib import admin

admin.site.register(Punn)
admin.site.register(Post)
admin.site.register(Tags)
admin.site.register(Reblog)
admin.site.register(Favorite)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(CommentVote)
admin.site.register(PunnVote)
admin.site.register(Image)


