from wagtail.core import blocks
from wagtail.core.blocks import (
    FloatBlock,
    ListBlock,
    RichTextBlock,
    TextBlock,
    URLBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class CTAButtonBlock(blocks.StructBlock):
    link = URLBlock()
    title = TextBlock()

    class Meta:
        template = "home/blocks/cta_button.html"


class CasinoCardBlock(blocks.StructBlock):
    title = TextBlock()
    subtitle = TextBlock()
    cta_button = CTAButtonBlock()
    review_score = FloatBlock()
    image = ImageChooserBlock()
    description = RichTextBlock()
    terms_and_conditions = RichTextBlock()

    class Meta:
        template = "home/blocks/casino_card.html"


class CasinoCardsBlock(blocks.StructBlock):
    title = TextBlock()
    casino_cards = ListBlock(CasinoCardBlock)

    class Meta:
        template = "home/blocks/casino_cards.html"


class FeatureBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = TextBlock()
    text = RichTextBlock()

    class Meta:
        template = "home/blocks/feature.html"


class FeaturesBlock(blocks.StructBlock):
    title = TextBlock()
    features = ListBlock(FeatureBlock)

    class Meta:
        template = "home/blocks/features.html"


HOMEPAGE_BODY_STREAMBLOCKS = (
    ("features", FeaturesBlock()),
    ("casino_cards", CasinoCardsBlock()),
)
