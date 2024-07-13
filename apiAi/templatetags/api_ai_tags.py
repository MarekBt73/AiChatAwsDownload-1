# C:\Users\Dell\work2\backend_www\backend\apiAi\templatetags\form_tags.py
# C:\Users\Dell\work2\backend_www\backend\apiAi\templatetags\api_ai_tags.py
from django import template

register = template.Library()


@register.filter(name="add_class2")
def add_class2(value, arg):
    return value.replace(
        '<div class="message-content">', f'<div class="message-content {arg}">'
    )
