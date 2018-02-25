# MP-FAQ application

### Installation

Install with pip:

```
$ pip install django-mp-faq
```

Add faq to settings.py:

```
INSTALLED_APPS = [
    ...
    'ordered_model',
    'modeltranslation',
    'faq',
]
```
Sync DB:

```
$ python manage.py migrate
$ python manage.py sync_translation_fields
```

## Template
```
{% load faq %}

{% get_faq_questions as faq_questions %}

{% for question in faq_questions %}
    {{ question.question }}
    {{ question.answer|safe }}
{% endfor %}
```

### Requirements

App require this packages:

* django-modeltranslation
* django-ordered-model
