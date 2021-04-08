
class FAQSettings(object):

    @property
    def INSTALLED_APPS(self):
        apps = super().INSTALLED_APPS + ['faq']

        if 'ordered_model' not in apps:
            apps.append('ordered_model')

        return apps


default = FAQSettings
