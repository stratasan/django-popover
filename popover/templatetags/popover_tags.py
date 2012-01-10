from django import template
from django.conf import settings
from popover.models import Popover

register = template.Library()

@register.inclusion_tag('popover/popover_link.html')
def popover(slug, content=None):
    if content:
        return {'popover':{'title': slug,'content': content},'STATIC_URL':settings.STATIC_URL}
    try:
        popover = Popover.objects.get(slug=slug)
    except:
        popover = None
    return { 'popover': popover,'STATIC_URL':settings.STATIC_URL }
