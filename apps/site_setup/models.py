from django.core.exceptions import ValidationError
from django.db import models

from apps.utils.files import resize_image, upload_to


class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    site_setup = models.ForeignKey(
        'SiteSetup',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text


def validate_image(image: models.ImageField):
    if not image.name.lower().endswith('.png'):
        raise ValidationError('Invalid image')


class SiteSetup(models.Model):
    class Meta:
        verbose_name = "Setup"
        verbose_name_plural = "Setup"

    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)

    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    fav_icon = models.ImageField(
        upload_to=upload_to,
        blank=True, default='',
        validators=[validate_image]
    )

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        current_favicon_name = str(self.fav_icon.name)
        super().save(*args, **kwargs)
        favicon_changed = False

        if self.fav_icon:
            favicon_changed = current_favicon_name != self.fav_icon.name

        if favicon_changed:
            resize_image(self.fav_icon, 32)
