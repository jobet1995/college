from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel
from .blocks import *

class HomePage(Page):
    template = "home/home_page.html"
    
    page_description = models.TextField(blank=True, null=True)
    
    content = StreamField([
        ("hero", HeroBlock()),
        ("rich_content", RichContentBlock()),
        ("features", FeatureBlock()),
        ("statistics", StatsBlock()),
        ("gallery", GalleryBlock()),
        ("testimonials", TestimonialBlock()),
        ("programs", ProgramListBlock()),
        ("events", EventBlock()),
        ("news", NewsBlock()),
        ("cta_button", ButtonBlock()),
    ], use_json_field=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('page_description'),
        FieldPanel('content'),
    ]

class AboutPage(Page):
    template = "home/about_page.html"

    page_description = models.TextField(blank=True, null=True)
    
    content = StreamField([
        ("hero", HeroBlock()),
        ("section_header", SectionHeaderBlock()),
        ("rich_content", RichContentBlock()),
        ("statistics", StatsBlock()),
        ("gallery", GalleryBlock()),
        ("testimonials", TestimonialBlock()),
        ("research", ResearchBlock()),
    ], use_json_field=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('page_description'),
        FieldPanel('content'),
    ]

class AcademicsPage(Page):
    template = "home/academics_page.html"

    page_description = models.TextField(blank=True, null=True)
    
    content = StreamField([
        ("hero", HeroBlock()),
        ("programs", ProgramListBlock()),
        ("rich_content", RichContentBlock()),
        ("statistics", StatsBlock()),
        ("gallery", GalleryBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("content"),
    ]

class AdmissionsPage(Page):
    template = "home/admissions_page.html"

    page_description = models.TextField(blank=True, null=True)
    
    content = StreamField([
        ("hero", HeroBlock()),
        ("steps", StepsBlock()),
        ("rich_content", RichContentBlock()),
        ("testimonials", TestimonialBlock()),
        ("cta_button", ButtonBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("content"),
    ]

class DepartmentsPage(Page):
    template = "home/departments_page.html"

    page_description = models.TextField(blank=True, null=True)
    
    content = StreamField([
        ("hero", HeroBlock()),
        ("section_header", SectionHeaderBlock()),
        ("faculty", FacultyListBlock()),
        ("programs", ProgramListBlock()),
        ("statistics", StatsBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("content"),
    ]

class FacultyPage(Page):
    template = "home/faculty_page.html"

    page_description = models.TextField(blank=True, null=True)
    
    content = StreamField([
        ("hero", HeroBlock()),
        ("faculty", FacultyListBlock()),
        ("statistics", StatsBlock()),
        ("testimonials", TestimonialBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("content"),
    ]

class CampusLifePage(Page):

    template ="home/campus_life_page.html"

    page_description = models.TextField(blank=True, null=True)

    content = StreamField([
        ("hero", HeroBlock()),
        ("gallery", GalleryBlock()),
        ("testimonials", TestimonialBlock()),
        ("rich_content", RichContentBlock()),
        ("events", EventBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("content"),
    ]

class ResearchPage(Page):

    template = "home/research_page.html"

    page_description = models.TextField(blank=True, null=True)
    
    content = StreamField([
        ("hero", HeroBlock()),
        ("research", ResearchBlock()),
        ("rich_content", RichContentBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("content"),
    ]

class NewsIndexPage(Page):
    template = "home/news_index_page.html"

    page_description = models.TextField(blank=True, null=True)
    
    content = StreamField([
        ("news_list", NewsBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("content"),
    ]

class NewsDetailPage(Page):

    template = "home/news_detail_page.html"

    page_description = models.TextField(blank=True, null=True)
    
    date = models.DateField()
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("date"),
        FieldPanel("body"),
    ]

class EventsIndexPage(Page):

    template = "home/events_index_page.html"

    page_description = models.TextField(blank=True, null=True)

    content = StreamField([
        ("events_list", EventBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("content"),
    ]

class EventsDetailPage(Page):

    template = "home/events_detail_page.html"

    page_description = models.TextField(blank=True, null=True)

    date = models.DateField()
    location = models.CharField(max_length=250, blank=True)
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("date"),
        FieldPanel("location"),
        FieldPanel("body"),
    ]

class ContactPage(Page):

    template = "home/contact_page.html"

    page_description = models.TextField(blank=True, null=True)
    
    content = StreamField([
        ("hero", HeroBlock()),
        ("contact_details", ContactDetailsBlock()),
        ("map", MapBlock()),
        ("contact_form", ContactFormBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("page_description"),
        FieldPanel("content"),
    ]