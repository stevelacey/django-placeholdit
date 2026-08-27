# -*- coding: utf-8 -*-
from django.urls import re_path
from django.views.decorators.cache import cache_page
from django_placeholdit import settings
from django_placeholdit.views import PlaceholderView

app_name = "placeholdit"

placeholder = cache_page(settings.PLACEHOLDIT_CACHE_SECONDS)(PlaceholderView.as_view())

kwargs = {
    'width':      r'(?P<width>\d+)',
    'height':     r'(?P<height>\d+)',
    'format':     r'(?P<format>gif|jpe?g|png)',
    'background': r'(?P<background>.*?)',
    'color':      r'(?P<color>.*?)',
    'text':       r'(?P<text>.*?)',
}

urlpatterns = [
    re_path(
        r'^{width}(?:x{height})?(?:\.{format})?(?:/{background}(?:/{color})?)?(?:&text={text})?$'.format(**kwargs),
        placeholder,
        name='placeholder',
    ),
]
