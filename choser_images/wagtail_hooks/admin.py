from wagtail_modeladmin.options import ModelAdmin, modeladmin_register

from choser_images.models import HomePage


@modeladmin_register
class HomePageAdmin(ModelAdmin):
    model = HomePage
    menu_label = "Home page"
    add_to_admin_menu = True
