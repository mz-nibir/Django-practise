from django import template

register = template.Library()

def my_fiter(value,args):
    return value + " " + args


register.filter('custom_filter',my_fiter)
