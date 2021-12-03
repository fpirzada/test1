from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import CasinoReview


@modeladmin_register
class CasinoReviewAdmin(ModelAdmin):
    model = CasinoReview
    menu_icon = "pick"
    list_display = ["title", "live"]
