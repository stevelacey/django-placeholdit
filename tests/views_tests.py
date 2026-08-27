from unittest.mock import patch

from wand.image import Image


def test_default_dimensions_and_format(client):
    response = client.get("/placeholders/160")

    assert response.status_code == 200
    assert response["Content-Type"] == "image/gif"

    with Image(blob=response.content) as image:
        assert image.width == 160
        assert image.height == 160


def test_custom_dimensions(client):
    response = client.get("/placeholders/240x160&text=Custom%20dimensions")

    with Image(blob=response.content) as image:
        assert image.width == 240
        assert image.height == 160


def test_custom_colors(client):
    response = client.get("/placeholders/160/F77A00/fff&text=Custom%20colors%21")

    assert response.status_code == 200


def test_custom_format(client):
    response = client.get("/placeholders/160.jpg/93C663/3F740E&text=gif/jpeg/png")

    assert response.status_code == 200
    assert response["Content-Type"] == "image/jpg"

    with Image(blob=response.content) as image:
        assert image.format.lower() in ("jpeg", "jpg")


def test_long_text_shrinks_the_font_to_fit(client):
    response = client.get("/placeholders/60&text=a%20moderately%20long%20label")

    assert response.status_code == 200


def test_font_path_is_applied_when_configured(client):
    with patch("django_placeholdit.views.Drawing") as mock_drawing:
        instance = mock_drawing.return_value.__enter__.return_value
        instance.get_font_metrics.return_value.text_width = 0

        with patch("django_placeholdit.views.settings") as mock_settings:
            mock_settings.PLACEHOLDIT_FONT_PATH = "/fonts/custom.ttf"

            response = client.get("/placeholders/160")

    assert response.status_code == 200
    assert instance.font == "/fonts/custom.ttf"
