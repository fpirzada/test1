from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from ..core.block import GridBlock
from ..core.models import PageBase
from .blocks import HOMEPAGE_BODY_STREAMBLOCKS


class HomePage(PageBase):
    body = StreamField(
        (HOMEPAGE_BODY_STREAMBLOCKS + (("row", GridBlock(HOMEPAGE_BODY_STREAMBLOCKS)),)), null=True, blank=True
    )

    content_panels = [StreamFieldPanel("body")]
