
from modeltranslation.translator import register, TranslationOptions

from faq.models import Question


@register(Question)
class QuestionTranslationOptions(TranslationOptions):

    fields = ('question', 'answer', )