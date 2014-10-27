import os
from django import template


register = template.Library()


@register.filter
def filename(value):
    return os.path.basename(value.file.name)


@register.filter
def just_date(value):
    if not value:
        return ''
    return value.date()
