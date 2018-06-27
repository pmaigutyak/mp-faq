
from modeltranslation.translator import translator

from faq.models import Question


translator.register(Question, fields=['question', 'answer'])
