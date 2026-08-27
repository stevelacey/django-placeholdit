# Django Placehold.it

[![PyPI](https://img.shields.io/pypi/v/django-placeholdit?style=flat-square)](https://pypi.org/project/django-placeholdit/)
[![CI](https://img.shields.io/github/actions/workflow/status/stevelacey/django-placeholdit/ci.yml?style=flat-square)](https://github.com/stevelacey/django-placeholdit/actions/workflows/ci.yml?query=branch:main)
[![Coverage](https://img.shields.io/codecov/c/github/stevelacey/django-placeholdit?style=flat-square)](https://codecov.io/gh/stevelacey/django-placeholdit)
[![Downloads](https://img.shields.io/pypi/dm/django-placeholdit?style=flat-square)](https://pypi.org/project/django-placeholdit/)
[![License](https://img.shields.io/github/license/stevelacey/django-placeholdit?style=flat-square)](https://github.com/stevelacey/django-placeholdit/blob/master/LICENSE.md)

A fully featured drop-in replacement of [placehold.it](http://placehold.it) for Django

| | | |
| --- | --- | --- |
| ![](https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/160.gif) | ![](https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/custom-dimensions.gif) | ![](https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/custom-text.gif) |
| ![](https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/custom-colors.gif) | ![](https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/automatically.gif)<br>![](https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/scaled.gif) | ![](https://raw.githubusercontent.com/stevelacey/django-placeholdit/master/examples/formats.jpg) |

## Features

- Everything [placehold.it](http://placehold.it) and [placeholder.com](http://placeholder.com) did
- Identical URL structure
- Improved font rendition and vertical text alignment

## Install

```sh
pip install django-placeholdit
```

Add django_placeholdit to your INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
    # ...
    "django_placeholdit",
]
```

Add the routes into your urls.py, feel free to customise the prefix or namespace, no trailing slash:

```python
urlpatterns = [
    # ...
    path("placeholders/", include("django_placeholdit.urls", namespace="placeholdit")),
]
```

## Configuration

The following options can be configured in your settings.py:

- `PLACEHOLDIT_CACHE_SECONDS` — Number of seconds to cache placeholders. Defaults to `86400 * 7` (a week)
- `PLACEHOLDIT_FONT_PATH` — Font path that locates the font to be used, e.g. `/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc`. Defaults to `None`

## Usage

In templates:

```django
<img src="{% url 'placeholdit:placeholder' width=160 %}">
<img src="{% url 'placeholdit:placeholder' width=240 height=160 text='Custom dimensions' %}">
<img src="{% url 'placeholdit:placeholder' width=160 text='Custom text!' %}">
<img src="{% url 'placeholdit:placeholder' width=160 background='F77A00' color='fff' text='Custom colors!' %}">
<img src="{% url 'placeholdit:placeholder' width=240 height=80 background='fbd206' color='fff' text='Automatically' %}">
<img src="{% url 'placeholdit:placeholder' width=240 height=80 background='fbd206' color='fff' text='scaled!' %}">
<img src="{% url 'placeholdit:placeholder' width=160 background='93C663' color='3F740E' text='gif/jpeg/png' format='jpg' %}">
```

Resulting in:

```html
<img src="http://example.com/placeholders/160">
<img src="http://example.com/placeholders/240x160&text=Custom%20dimensions">
<img src="http://example.com/placeholders/160&text=Custom%20text%21">
<img src="http://example.com/placeholders/160/F77A00/fff&text=Custom%20colors%21">
<img src="http://example.com/placeholders/240x80/fbd206/fff&text=Automatically">
<img src="http://example.com/placeholders/240x80/fbd206/fff&text=scaled%21">
<img src="http://example.com/placeholders/160.jpg/93C663/3F740E&text=gif/jpeg/png">
```

## Development

```bash
poetry install
poetry run pytest
poetry run ruff check .
```

## License

MIT
