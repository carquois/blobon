from punns.models import Punn
from earnings.models import Earning
from punns.models import Favorite 
from punns.models import Tags
from punns.models import Cat 
from punns.models import Reblog
from posts.models import Link
from accounts.models import UserProfile
from blogs.models import Comment
from notifications.models import Invitation
from images.models import Image
from votes.models import CommentVote, PunnVote
from django.contrib import admin
from blogs.models import Blog, Tag, Category, Post, Model, ModelField, ModelData, ModelFieldData
from blogs.models import Page
from posts.models import Image
from posts.models import Album
from posts.models import Video 
from blogs.models import Page
from blogs.models import Subscription
from blogs.models import Info_email
from blogs.models import Language
from blogs.models import Translation
from blogs.models import Rss
from books.models import Client
from books.models import Invoice
from books.models import Project
from books.models import Tax
from books.models import Expense, Vendor, Report
from books.models import Task
from books.models import Time
from books.models import Item
from blogs.models import Menu
from blogs.models import MenuItem
from blogs.models import Template

class PunnAdmin(admin.ModelAdmin):
    exclude = ('original_punn',)

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
admin.site.register(Punn, PunnAdmin)
admin.site.register(Link)
admin.site.register(Video)
admin.site.register(Blog)
admin.site.register(Page)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
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
admin.site.register(Subscription)
admin.site.register(Info_email)
admin.site.register(Language)
admin.site.register(Translation)
admin.site.register(Client)
admin.site.register(Invoice)
admin.site.register(Project)
admin.site.register(Tax)
admin.site.register(Expense)
admin.site.register(Task)
admin.site.register(Time)
admin.site.register(Item)
admin.site.register(Rss)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(Template)
admin.site.register(Vendor)
admin.site.register(Report)
admin.site.register(ModelField)
admin.site.register(Model)
admin.site.register(ModelData)
admin.site.register(ModelFieldData)
