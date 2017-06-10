
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):

    question = models.CharField(_('Question'), max_length=255, unique=True)

    answer = models.TextField(_('Answer'), max_length=10000)

    def __unicode__(self):
        return self.question

    class Meta:
        verbose_name = _("Frequent asked question")
        verbose_name_plural = _("Frequently asked questions")
