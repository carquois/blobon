from django.db import models
from punns.models import Punn
from django.contrib.auth.models import User
from django.forms import ImageField, EmailField, ModelForm, CharField, PasswordInput
from django import forms
from punns.utils import BASE10, BASE62, baseconvert
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext as _

class Comment(models.Model):
    content = models.TextField(max_length=10000)
    base62id = models.CharField(max_length=140, blank=True)
    author = models.ForeignKey(User)
    punn = models.ForeignKey(Punn)
    karma = models.IntegerField(default=0)
    parent = models.ForeignKey('self',  null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    pub_date = models.DateTimeField(auto_now = True,  null=True, blank=True)
    def __unicode__(self):
        return self.content
    def save(self):
        super(Comment, self).save()
        if not self.base62id:
            self.base62id = baseconvert(str(self.id),BASE10,BASE62)
            self.save()
    @models.permalink
    def get_absolute_url(self):
        return ('punn.views.comment', [str(self.base62id)])

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': Textarea(attrs={'placeholder': _('Soumettre un commentaire...'),
                                       'id': 'comment-box', 
                                       'rows': '1'}),
        }

