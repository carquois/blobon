from punns.models import Punn
from earnings.models import Earning
from punns.models import Favorite 
from punns.models import Tags
from punns.models import Cat 
from punns.models import Reblog
from posts.models import Link
from accounts.models import UserProfile
from comments.models import Comment
from notifications.models import Invitation
from images.models import Image
from votes.models import CommentVote, PunnVote
from django.contrib import admin
from blogs.models import Blog
from posts.models import Post
from posts.models import Image
from posts.models import Album
from pages.models import Page

class PunnAdmin(admin.ModelAdmin):
    exclude = ('original_punn',)
admin.site.register(Punn, PunnAdmin)
admin.site.register(Link)
admin.site.register(Post)
admin.site.register(Page)
admin.site.register(Blog)
admin.site.register(Invitation)
admin.site.register(Album)
admin.site.register(Earning)
admin.site.register(Tags)
admin.site.register(Cat)
admin.site.register(Reblog)
admin.site.register(Favorite)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(CommentVote)
admin.site.register(PunnVote)
admin.site.register(Image)


