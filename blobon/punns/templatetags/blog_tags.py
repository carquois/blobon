from django import template
register = template.Library()
#import re

#re_nobr = re.compile("<br />")
register = template.Library()

#def do_nobr(parser, token):
#       nodelist = parser.parse(('endnobr',))
#       parser.delete_first_token()
#       return NobrNode(nodelist)

#class NobrNode(template.Node):
#    def __init__(self, nodelist):
#        self.nodelist = nodelist
#    def render(self, context):
#        rendered = self.nodelist.render(context).strip()
#        return re_nobr.sub("", rendered)


class UltraRender(template.Node):

    def __init__(self, obj_and_field):
        self.obj = template.Variable(obj_and_field.split('.')[0])
        self.t = obj_and_field.split('.')[1]

    def render(self, context):
        obj = self.obj.resolve(context)
        t = template.Template(getattr(obj, self.t))
        rendered_field = t.render(context)
        return template.defaultfilters.safe(rendered_field)

@register.tag
def ultrarender(parser, token):
    bits = token.contents.split()
    return UltraRender(bits[1])
