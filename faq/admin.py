
import faq.translation

from django.apps import apps
from django.db import models
from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from faq.models import Question


class QuestionAdmin(TranslationAdmin):

    def __init__(self, *args, **kwargs):

        if apps.is_installed('ckeditor_uploader'):
            from ckeditor_uploader.widgets import CKEditorUploadingWidget
            self.formfield_overrides.update({
                models.TextField: {'widget': CKEditorUploadingWidget}
            })

        elif apps.is_installed('ckeditor'):
            from ckeditor.widgets import CKEditorWidget
            self.formfield_overrides.update({
                models.TextField: {'widget': CKEditorWidget}
            })

        super(QuestionAdmin, self).__init__(*args, **kwargs)


admin.site.register(Question, QuestionAdmin)
