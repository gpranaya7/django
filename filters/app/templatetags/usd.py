from django import template
register=template.Library()
def swapping(data):
    return data.swapcase()
register.filter('swapcase',swapping)
@register.filter()
def splitting(data,val):
    return data.split(val)
