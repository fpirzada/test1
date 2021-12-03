from django.templatetags.static import static
from django.utils.html import format_html
from wagtail.core import hooks


@hooks.register("construct_main_menu")
def hide_snippets_menu_item(request, menu_items):
    """
    Hides snippets from the main nav. Use ModelAdmin for snippets (aka normal Django models) instead.
    More info: https://docs.wagtail.io/en/stable/reference/contrib/modeladmin/index.html
    """
    menu_items[:] = [item for item in menu_items if item.name != "snippets"]


@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """
    Add custom stylesheet for the admin.
    """
    return format_html('<link rel="stylesheet" href="{}">', static("core/admin/css/admin.css"))
