from django import template
from django.template.defaultfilters import stringfilter

#FILTRE
# register = template.Library()

# @register.filter
# @stringfilter
# def transform(value):
#     return value +"1"


#BALISE

register = template.Library()

@register.simple_tag
def hello(username):
    return f"hello {username} !"