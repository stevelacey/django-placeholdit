# -*- coding: utf-8 -*-
from django.conf import settings

PLACEHOLDIT_CACHE_SECONDS = getattr(settings, 'PLACEHOLDIT_CACHE_SECONDS', 86400 * 7)
