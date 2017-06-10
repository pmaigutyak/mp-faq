
from django.apps import apps
from django import template


register = template.Library()


@register.simple_tag
def get_faq_questions():
    return apps.get_model('faq', 'Question').objects.all()
