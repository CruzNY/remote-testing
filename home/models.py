from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    homePageMessage = RichTextField(default='alex')
    aboutMe = RichTextField(default='alex')
    aboutThisWebsite = RichTextField(default='alex')

    content_panels = Page.content_panels + [
        FieldPanel('homePageMessage'),
        FieldPanel('aboutMe'),
        FieldPanel('aboutThisWebsite'),
    ]
