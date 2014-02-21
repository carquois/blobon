from django import template
register = template.Library()

class UltraRender(template.Node):

    def __init__(self, obj_and_field):
        self.obj = template.Variable(obj_and_field.split('.')[0])
        self.t = obj_and_field.split('.')[1]

    def render(self, context):
        obj = self.obj.resolve(context)
        t = template.Template(getattr(obj, self.t))
        rendered_field = t.render(context)
        return template.defaultfilters.linebreaks(rendered_field)

@register.tag
def ultrarender(parser, token):
    bits = token.contents.split()
    return UltraRender(bits[1])
