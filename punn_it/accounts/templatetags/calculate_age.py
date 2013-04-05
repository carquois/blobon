import datetime
from django import template
register = template.Library()

@register.filter("age")
def age(birthday, fromD=None):
    """
    Use this filter with a users datetime object:
    {{ this_user.profile.birthday|age }}
    """
    if fromD is None:
        fromD = datetime.date.today()
    return (fromD.year - birthday.year) - int((fromD.month, fromD.day) < (birthday.month, birthday.day))