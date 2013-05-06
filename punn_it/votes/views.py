from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from comments.models import Comment
from punns.models import Punn
from votes.models import CommentVote, PunnVote

@login_required
def up(request, id):
      punn = get_object_or_404(Punn, id=id)
      punnvote(request, 'U', punn)
      return HttpResponseRedirect( punn.get_absolute_url() )

@login_required
def down(request, id):
      punn = get_object_or_404(Punn, id=id)
      punnvote(request, 'D', punn)
      return HttpResponseRedirect( punn.get_absolute_url() )

@login_required
def punnvote(request, side, punn):
      if PunnVote.objects.filter(punn=punn).filter(user=request.user).exists():
        v = PunnVote.objects.filter(punn=punn).filter(user=request.user)
        if v[0].vote == side:
          v[0].delete()
        else:
          v[0].delete()
          vote = PunnVote(punn=punn, user=request.user, vote=side)
          vote.save()
      else: 
        vote = PunnVote(punn=punn, user=request.user, vote=side)
        vote.save()

@login_required
def commentvote(request, side, comment):
      if CommentVote.objects.filter(comment=comment).filter(user=request.user).exists():
        v = CommentVote.objects.filter(comment=comment).filter(user=request.user)
        if v[0].vote == side:
          v[0].delete()
        else:
          v[0].delete()
          vote = CommentVote(comment=comment, user=request.user, vote=side)
          vote.save()
      else: 
        vote = CommentVote(comment=comment, user=request.user, vote=side)
        vote.save()

@login_required
def commentup(request, id):
      comment = get_object_or_404(Comment, id=id)
      commentvote(request, 'U', comment)
      return HttpResponseRedirect( comment.punn.get_absolute_url() )

@login_required
def commentdown(request, id):
      comment = get_object_or_404(Comment, id=id)
      commentvote(request, 'D', comment)
      return HttpResponseRedirect( comment.punn.get_absolute_url() )

