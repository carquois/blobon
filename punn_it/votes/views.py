from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from comments.models import Comment
from punns.models import Punn
from votes.models import CommentVote, PunnVote

@login_required
def up(request, id):
      punn = get_object_or_404(Punn, id=id)
      v = PunnVote.objects.filter(punn=punn).filter(user=request.user).filter(vote='U')
      if v.count() == 0:
        vote = PunnVote(punn=punn, user=request.user, vote='U')
        vote.save()
      elif v.count() == 1:
        v[0].delete()
      return HttpResponseRedirect( punn.get_absolute_url() )

@login_required
def down(request, id):
      punn = get_object_or_404(Punn, id=id)
      v = PunnVote.objects.filter(punn=punn).filter(user=request.user).filter(vote='D')
      if v.count() == 0:
        vote = PunnVote(punn=punn, user=request.user, vote='D')
        vote.save()
      elif v.count() == 1:
        v[0].delete()
      return HttpResponseRedirect( punn.get_absolute_url() )

@login_required
def voteup(request, id):
      comment = get_object_or_404(Comment, id=id)
      punn = comment.punn
      v = CommentVote.objects.filter(comment=comment).filter(user=request.user).filter(vote='U')
      if v.count() == 0:
        vote = CommentVote(comment=comment, user=request.user, vote='U')
        vote.save()
      elif v.count() == 1:
        v[0].delete() 
      return HttpResponseRedirect( punn.get_absolute_url() )

@login_required
def votedown(request, id):
      comment = get_object_or_404(Comment, id=id)
      punn = comment.punn
      v = CommentVote.objects.filter(comment=comment).filter(user=request.user).filter(vote='D')
      if v.count() == 0:
        vote = CommentVote(comment=comment, user=request.user, vote='D')
        vote.save()
      elif v.count() == 1:
        v[0].delete() 
      return HttpResponseRedirect( punn.get_absolute_url() )
