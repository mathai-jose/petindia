from django import template

register = template.Library()

@register.filter
def remove_asterisks(value):
    return value.replace('***', '')
