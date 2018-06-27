
from django.db import models
from django.utils.translation import ugettext_lazy as _

from ordered_model.models import OrderedModel


class Question(OrderedModel):

    question = models.CharField(_('Question'), max_length=255, unique=True)

    answer = models.TextField(_('Answer'), max_length=10000)

    def __str__(self):
        return self.question

    class Meta(OrderedModel.Meta):
        verbose_name = _("Frequent asked question")
        verbose_name_plural = _("Frequently asked questions")
