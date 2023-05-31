from django import template
from django.conf import settings

register = template.Library()


@register.filter
def mediapath(media_path):
    return f"{settings.MEDIA_URl, media_path}"


@register.simple_tag
def mediapath(media_path):
    return f"{settings.MEDIA_URl, media_path}"
