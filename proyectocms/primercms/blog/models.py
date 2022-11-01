from django.db import models 
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]

class BlogPage(Page):
	date = models.DateField("Post date")
	intro = RichTextField(blank=True, max_length="250")
	body = RichTextField(blank=True)

	content_panels = Page.content_panels + [
		FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]