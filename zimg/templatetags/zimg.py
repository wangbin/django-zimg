# coding: utf-8

from django import template
from django.utils.http import urlencode

register = template.Library()

@register.simple_tag(name="zimg")
def zimg(url, **kwargs):
    return '{0}?{1}'.format(url, urlencode(kwargs))
    
