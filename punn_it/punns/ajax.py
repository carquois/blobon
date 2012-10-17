from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from punns.models import Punn
from votes.models import PunnVote
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

@dajaxice_register
def up(request, auth_userid, punnid, karma):
    punn = Punn.objects.get(pk=int(punnid))
    user = User.objects.get(pk=int(auth_userid))
    if PunnVote.objects.filter(user=user).filter(punn=punn):
      if PunnVote.objects.filter(user=user).filter(punn=punn).filter(vote='U'):
        vote = PunnVote.objects.filter(user=user).filter(punn=punn).filter(vote='U')[0]
        vote.delete()
        dajax = Dajax()
        result = int(karma)
        dajax.assign('#karma','value',str(result))
        dajax.remove_css_class('#upbutton','btn-primary')
        return dajax.json()
      else:
        vote = PunnVote.objects.filter(user=user).filter(punn=punn).filter(vote='D')[0]
        vote.vote = 'U'
        vote.save()
        dajax = Dajax()
        result = int(karma) + 1
        dajax.assign('#karma','value',str(result))
        dajax.remove_css_class('#downbutton','btn-primary')
        dajax.add_css_class('#upbutton','btn-primary')
        return dajax.json()
    else:
      result = int(karma) + 1 
      vote = PunnVote(user=user, punn=punn, vote='U')
      vote.save()
      dajax = Dajax()
      dajax.assign('#karma','value',str(result))
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
        result = int(karma)
        dajax.assign('#karma','value',str(result))
        dajax.remove_css_class('#downbutton','btn-primary')
        return dajax.json()
      else:
        vote = PunnVote.objects.filter(user=user).filter(punn=punn).filter(vote='U')[0]
        vote.vote = 'D'
        vote.save()
        dajax = Dajax()
        result = int(karma) - 1
        dajax.assign('#karma','value',str(result))
        dajax.remove_css_class('#upbutton','btn-primary')
        dajax.add_css_class('#downbutton','btn-primary')
        return dajax.json()
    else:
      result = int(karma) - 1  
      vote = PunnVote(user=user, punn=punn, vote='D')
      vote.save()
      dajax = Dajax()
      dajax.assign('#karma','value',str(result))
      dajax.add_css_class('#downbutton','btn-primary')
      return dajax.json()

@dajaxice_register
def changeImage(request, image):
    dajax = Dajax()
    dajax.assign('#mainImage','src', image)
    return dajax.json()
