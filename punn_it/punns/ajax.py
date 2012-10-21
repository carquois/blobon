from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from punns.models import Punn
from comments.models import Comment
from votes.models import PunnVote, CommentVote
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from punns.views import linkify 
import markdown

@dajaxice_register
def up(request, auth_userid, punnid, karma):
    punn = Punn.objects.get(pk=int(punnid))
    user = User.objects.get(pk=int(auth_userid))
    if PunnVote.objects.filter(user=user).filter(punn=punn):
      if PunnVote.objects.filter(user=user).filter(punn=punn).filter(vote='U'):
        vote = PunnVote.objects.filter(user=user).filter(punn=punn).filter(vote='U')[0]
        vote.delete()
        dajax = Dajax()
        karma = getKarma(punn) 
        dajax.assign('#karma','value',str(karma))
        dajax.remove_css_class('#upbutton','btn-primary')
        return dajax.json()
      else:
        vote = PunnVote.objects.filter(user=user).filter(punn=punn).filter(vote='D')[0]
        vote.vote = 'U'
        vote.save()
        dajax = Dajax()
        karma = getKarma(punn)
        dajax.assign('#karma','value',str(karma))
        dajax.remove_css_class('#downbutton','btn-primary')
        dajax.add_css_class('#upbutton','btn-primary')
        return dajax.json()
    else:
      vote = PunnVote(user=user, punn=punn, vote='U')
      vote.save()
      dajax = Dajax()
      karma = getKarma(punn)
      dajax.assign('#karma','value',str(karma))
      dajax.add_css_class('#upbutton','btn-primary')
      return dajax.json()

@dajaxice_register
def down(request, auth_userid, punnid, karma):
    punn = Punn.objects.get(pk=int(punnid))
    user = User.objects.get(pk=int(auth_userid))
    if PunnVote.objects.filter(user=user).filter(punn=punn):
      if PunnVote.objects.filter(user=user).filter(punn=punn).filter(vote='D'):
        vote = PunnVote.objects.filter(user=user).filter(punn=punn).filter(vote='D')[0]
        vote.delete()
        dajax = Dajax()
        karma = getKarma(punn) 
        dajax.assign('#karma','value',str(karma))
        dajax.remove_css_class('#downbutton','btn-primary')
        return dajax.json()
      else:
        vote = PunnVote.objects.filter(user=user).filter(punn=punn).filter(vote='U')[0]
        vote.vote = 'D'
        vote.save()
        dajax = Dajax()
        karma = getKarma(punn) 
        dajax.assign('#karma','value',str(karma))
        dajax.remove_css_class('#upbutton','btn-primary')
        dajax.add_css_class('#downbutton','btn-primary')
        return dajax.json()
    else:
      vote = PunnVote(user=user, punn=punn, vote='D')
      vote.save()
      dajax = Dajax()
      karma = getKarma(punn) 
      dajax.assign('#karma','value',str(karma))
      dajax.add_css_class('#downbutton','btn-primary')
      return dajax.json()

@dajaxice_register
def changeImage(request, image):
    dajax = Dajax()
    dajax.assign('#mainImage','src', image)
    return dajax.json()

@dajaxice_register
def loadComments(request, punnid):
    dajax = Dajax()
    punn = Punn.objects.get(pk=int(punnid))
    comment_list = Comment.objects.filter(punn=punn).order_by('-pub_date')[:10]
    dajax.remove('#loading-comments')
    for comment in comment_list:
        comment.content = linkify(comment.content)
        comment.content = markdown.markdown(comment.content)
        dajax.append('#comments', 'innerHTML', '<button id="upbutton" class="btn {% if vote == "U" %}btn-primary{% endif %}" onclick="up();">Up</button>')
        dajax.append('#comments', 'innerHTML', '<input type="text" value="{{ karma }}" id="karma" class="input-small">')
        dajax.append('#comments', 'innerHTML', '<button id="downbutton" class="btn {% if vote == "D" %}btn-primary{% endif %}" onclick="down();">Down</button>')
        dajax.append('#comments', 'innerHTML', str(comment.content))
    return dajax.json()

def getKarma(punn):
    votesup = PunnVote.objects.filter(punn=punn).filter(vote='U')
    votesdown = PunnVote.objects.filter(punn=punn).filter(vote='D')
    return votesup.count() - votesdown.count()

