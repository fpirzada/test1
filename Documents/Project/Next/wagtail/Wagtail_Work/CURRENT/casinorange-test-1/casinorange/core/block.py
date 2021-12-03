from django.utils.translation import gettext_lazy as _
from wagtail.core import blocks

from .choices import ColumnSizeChoices


class BaseLayoutBlock(blocks.StructBlock):
    """
    Common attributes for all layout blocks.
    """

    content_streamblocks = []
    content_label = _("Content")

    def __init__(self, local_blocks=None, **kwargs):
        if not local_blocks and self.content_streamblocks:
            local_blocks = self.content_streamblocks

        if local_blocks:
            local_blocks = (("content", blocks.StreamBlock(local_blocks, label=self.content_label)),)

        super().__init__(local_blocks, **kwargs)


class ColumnBlock(BaseLayoutBlock):
    """
    Renders content in a column.
    """

    column_size = blocks.ChoiceBlock(
        choices=ColumnSizeChoices.choices,
        default=ColumnSizeChoices.FULL,
        required=False,
        label=_("Column size"),
    )

    class Meta:
        template = "core/blocks/column_block.html"
        icon = "placeholder"
        label = "Column"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        context.update({"column_css_class": self.get_column_css_class(value["column_size"])})
        return context

    def get_column_css_class(self, column_size):
        return {
            "HALF": "col-span-6",
            "THIRD": "col-span-4",
        }.get(column_size, "col-span-full")


class GridBlock(BaseLayoutBlock):
    """
    Renders a row of columns.
    """

    content_label = _("Columns")

    class Meta:
        template = "core/blocks/grid_block.html"
        icon = "fa-columns"
        label = _("Responsive Grid Row")

    def __init__(self, local_blocks=None, **kwargs):
        super().__init__(local_blocks=[("content", ColumnBlock(local_blocks))])
