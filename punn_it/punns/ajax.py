from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from punns.models import Punn

@dajaxice_register
def up(request, karma, punnid):
    dajax = Dajax()
    result = int(karma) + 1 
    dajax.assign('#karma','value',str(result))
    return dajax.json()

@dajaxice_register
def down(request, karma, punnid):
    dajax = Dajax()
    result = int(karma) - 1 
    dajax.assign('#karma','value',str(result))
    return dajax.json()
