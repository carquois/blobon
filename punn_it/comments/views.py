from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from comments.models import Comment
from punns.models import Punn

@login_required
def delete(request, id):
      comment = get_object_or_404(Comment, id=id)
      punn = comment.punn
      if request.user == comment.author:
        comment.delete()
      return HttpResponseRedirect( punn.get_absolute_url() )

