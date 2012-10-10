from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from punns.models import Punn
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _

@login_required
@dajaxice_register
def up(request, karma, punnid):
    try:
        p = Punn.objects.get(pk=punnid)
        p.karma = p.karma+1
        p.save()
        dajax = Dajax()
        result = int(karma) + 1 
        dajax.assign('#karma','value',str(result))
        dajax.add_css_class('#upbutton','btn-primary')
        return dajax.json()
    except Punn.DoesNotExist:
        dajax = Dajax()
        dajax.alert('Something went wrong')
        return dajax.json()

@dajaxice_register
def down(request, karma, punnid):
    dajax = Dajax()
    result = int(karma) - 1 
    dajax.assign('#karma','value',str(result))
    dajax.add_css_class('#downbutton','btn-primary')
    return dajax.json()
