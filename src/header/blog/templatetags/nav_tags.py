from django import template
from django.db.models import Count, F
from django.core.cache import cache



register = template.Library()


@register.inclusion_tag("admin/navbar.html")
def show_categories(user):
    if user.is_authenticated:
        group = user.groups.all()[0].name
    else:
        group = "Free"
    return {"user":user, "group":group}