from django import template

register = template.Library()

def my_fiter(value):
    return value + " This is starting from Custom filter"


register.filter('custom_filter',my_fiter)
