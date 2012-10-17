from django.db import models
from django.contrib.auth.models import User
from comments.models import Comment
from punns.models import Punn
from django.utils.translation import ugettext as _

VOTE_CHOICES = (
    ('1',  _('Vote up')),
    ('0',  _('Rescind')),
    ('-1', _('Vote down')),
)

class CommentVote(models.Model):
    comment = models.ForeignKey(Comment)
    user    = models.ForeignKey(User)
    vote    = models.CharField(max_length=1, choices=VOTE_CHOICES)

class PunnVote(models.Model):
    punn = models.ForeignKey(Punn)
    user = models.ForeignKey(User)
    vote = models.CharField(max_length=1, choices=VOTE_CHOICES)
