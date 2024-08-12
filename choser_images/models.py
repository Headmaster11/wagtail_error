from wagtail.models import Orderable
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Orderable, Page):
    body = StreamField([
        ('image', ImageChooserBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
