from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


def setup_settings(settings, is_prod, **kwargs):

    settings['INSTALLED_APPS'] += [
        app for app in [
            'faq',
            'ordered_model'
        ] if app not in settings['INSTALLED_APPS']
    ]


class FAQConfig(AppConfig):
    name = 'faq'
    verbose_name = _("FAQ")


default_app_config = 'faq.FAQConfig'
