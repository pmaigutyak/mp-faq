
from importlib import import_module

from django.apps import apps
from django.db import models
from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from faq.models import Question


def _get_question_admin_base_class():

    if apps.is_installed('modeltranslation'):
        return import_module('modeltranslation.admin').TranslationAdmin

    return admin.ModelAdmin


@admin.register(Question)
class QuestionAdmin(_get_question_admin_base_class(), OrderedModelAdmin):

    list_display = ['question', 'move_up_down_links']

    def __init__(self, *args, **kwargs):

        if apps.is_installed('ckeditor_uploader'):
            from ckeditor_uploader.widgets import CKEditorUploadingWidget
            self.formfield_overrides = {
                models.TextField: {'widget': CKEditorUploadingWidget}
            }

        elif apps.is_installed('ckeditor'):
            from ckeditor.widgets import CKEditorWidget
            self.formfield_overrides = {
                models.TextField: {'widget': CKEditorWidget}
            }

        super().__init__(*args, **kwargs)
