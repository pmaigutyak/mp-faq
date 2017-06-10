from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FAQConfig(AppConfig):
    name = 'faq'
    verbose_name = _("FAQ")


default_app_config = 'faq.FAQConfig'

__version__ = '1.0'
