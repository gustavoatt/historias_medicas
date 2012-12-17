from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from re import sub


register = template.Library()

@register.filter(name='add_placeholder')
@stringfilter
def add_placeholder(tag, placeholder):
	return mark_safe(sub(r'(>$)|(/>$)', ' placeholder="{}">'.format(placeholder), tag.strip()))
