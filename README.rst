Django Placehold.it
===================

A fully featured drop-in replacement of `placehold.it`_ for Django

+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| .. image:: https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/160.gif           | .. image:: https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/custom-dimensions.gif | .. image:: https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/custom-text.gif |
+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| .. image:: https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/custom-colors.gif | .. image:: https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/automatically.gif     | .. image:: https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/formats.jpg     |
|                                                                                                              +------------------------------------------------------------------------------------------------------------------+                                                                                                            |
|                                                                                                              | .. image:: https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/scaled.gif            |                                                                                                            |
+--------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

Features
--------

- Everything `placehold.it`_ does
- Identical URL structure
- Improved font rendition and vertical text alignment

Installation
------------
Install from PyPi:

You can pip install the app directly from GitHub:

::

    $ pip install git+git://github.com/stevelacey/django-placeholdit.git#egg=DjangoPlaceholdit

Alternatively, you can install from PyPi:

::

    $ pip install django-placeholdit

Add django_placeholdit to your INSTALLED_APPS in settings.py:

::

    INSTALLED_APPS = (
        # ...
        'django_placeholdit',
    )

Add django_placeholdit routes into your urls.py:

::

    urlpatterns = patterns(
        # ...
        url(r'^placeholders', include('django_placeholdit.urls', namespace='placeholdit')),
    )

Configuration
-------------
The following options can be configured in your settings.py:

``PLACEHOLDIT_CACHE_SECONDS`` # Number of seconds to cache placeholders. Defaults to `86400 * 7` (a week)

Usage
-----

In templates:

::

    <img src="{% url 'placeholdit:placeholder' width=160 %}">
    <img src="{% url 'placeholdit:placeholder' width=240 height=160 text='Custom dimensions' %}">
    <img src="{% url 'placeholdit:placeholder' width=160 text='Custom text!' %}">
    <img src="{% url 'placeholdit:placeholder' width=160 background='F77A00' color='fff' text='Custom colors!' %}">
    <img src="{% url 'placeholdit:placeholder' width=240 height=80 background='fbd206' color='fff' text='Automatically' %}">
    <img src="{% url 'placeholdit:placeholder' width=240 height=80 background='fbd206' color='fff' text='scaled!' %}">
    <img src="{% url 'placeholdit:placeholder' width=160 background='93C663' color='3F740E' text='gif/jpeg/png' format='jpg' %}">

Resulting in:

::

    <img src="http://example.com/placeholders/160">
    <img src="http://example.com/placeholders/240x160&text=Custom%20dimensions">
    <img src="http://example.com/placeholders/160&text=Custom%20text%21">
    <img src="http://example.com/placeholders/160/F77A00/fff&text=Custom%20colors%21">
    <img src="http://example.com/placeholders/240x80/fbd206/fff&text=Automatically">
    <img src="http://example.com/placeholders/240x80/fbd206/fff&text=scaled%21">
    <img src="http://example.com/placeholders/160.jpg/93C663/3F740E&text=gif/jpeg/png">

Contributing
------------
Feel free to `fork django-placeholdit <https://github.com/stevelacey/django-placeholdit>`_
on GitHub! I'd love to see your pull requests.

.. _placehold.it: http://placehold.it
