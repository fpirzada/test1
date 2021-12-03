from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.core.models import Page
from wagtail.documents.models import AbstractDocument
from wagtail.images.models import AbstractImage, AbstractRendition


class PageBase(Page):
    """
    The default Base class for any page on the project.

    Can be later used to add customizations that should be inherited by all pages.
    """

    class Meta:
        abstract = True


class CustomDocument(AbstractDocument):
    """
    An extension of the default Wagtail Document model.
    """

    admin_form_fields = ("title", "file", "collection", "tags")

    class Meta(AbstractDocument.Meta):
        permissions = [
            ("choose_document", "Can choose document"),
        ]


class CustomImage(AbstractImage):
    """
    An extension of the default Wagtail Image model.
    """

    admin_form_fields = (
        "title",
        "file",
        "collection",
        "tags",
        "focal_point_x",
        "focal_point_y",
        "focal_point_width",
        "focal_point_height",
    )

    class Meta(AbstractImage.Meta):
        verbose_name = _("image")
        verbose_name_plural = _("images")
        permissions = [
            ("choose_image", "Can choose image"),
        ]


class CustomImageRendition(AbstractRendition):
    """
    A rendition for the custom image model.
    """

    image = models.ForeignKey(CustomImage, on_delete=models.CASCADE, related_name="renditions")

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)
