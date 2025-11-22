from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


# ============================================================
#  GLOBAL REUSABLE BLOCKS
# ============================================================

class HeroBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=150)
    subtitle = blocks.TextBlock(required=False)
    background_image = ImageChooserBlock()
    overlay_opacity = blocks.FloatBlock(default=0.45)
    align = blocks.ChoiceBlock(choices=[
        ("left", "Left"),
        ("center", "Center"),
        ("right", "Right"),
    ], default="center")
    cta_primary_label = blocks.CharBlock(required=False, max_length=60)
    cta_primary_link = blocks.URLBlock(required=False)
    cta_secondary_label = blocks.CharBlock(required=False, max_length=60)
    cta_secondary_link = blocks.URLBlock(required=False)

    class Meta:
        icon = "image"
        label = "Hero Banner"
        template = "blocks/hero_block.html"
        help_text = "High-impact fullscreen section for page headers."


class SectionHeaderBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=150)
    subtitle = blocks.TextBlock(required=False)
    alignment = blocks.ChoiceBlock(choices=[
        ("left", "Left"),
        ("center", "Center"),
        ("right", "Right"),
    ], default="center")

    class Meta:
        icon = "title"
        label = "Section Header"
        template = "blocks/section_header_block.html"


class RichContentBlock(blocks.RichTextBlock):
    class Meta:
        icon = "doc-full"
        label = "Rich Content"
        template = "blocks/rich_content_block.html"


class ButtonBlock(blocks.StructBlock):
    label = blocks.CharBlock(max_length=50)
    link = blocks.URLBlock()
    style = blocks.ChoiceBlock(choices=[
        ("primary", "Primary"),
        ("secondary", "Secondary"),
        ("outline", "Outline")
    ], default="primary")

    class Meta:
        icon = "link"
        label = "Button"
        template = "blocks/button_block.html"


# ============================================================
#  FEATURE BLOCKS
# ============================================================

class FeatureItem(blocks.StructBlock):
    icon = blocks.CharBlock(required=False, help_text="Icon class name (e.g., 'ri-star-line')")
    title = blocks.CharBlock(max_length=120)
    description = blocks.TextBlock()

    class Meta:
        icon = "star"
        label = "Feature Item"
        template = "blocks/feature_item.html"


class FeatureBlock(blocks.StructBlock):
    section_header = SectionHeaderBlock(required=False)
    items = blocks.ListBlock(FeatureItem)

    class Meta:
        icon = "list-ul"
        label = "Features Section"
        template = "blocks/feature_block.html"


# ============================================================
#  STATISTICS BLOCK
# ============================================================

class StatItem(blocks.StructBlock):
    value = blocks.CharBlock(max_length=20)
    label = blocks.CharBlock(max_length=150)
    icon = blocks.CharBlock(required=False)

    class Meta:
        icon = "pick"
        label = "Statistic Item"
        template = "blocks/stat_item.html"


class StatsBlock(blocks.StructBlock):
    items = blocks.ListBlock(StatItem)

    class Meta:
        icon = "table"
        label = "Statistics Section"
        template = "blocks/stats_block.html"


# ============================================================
#  GALLERY BLOCK
# ============================================================

class GalleryBlock(blocks.StructBlock):
    section_header = SectionHeaderBlock(required=False)
    images = blocks.ListBlock(ImageChooserBlock())
    layout = blocks.ChoiceBlock(choices=[
        ("grid", "Grid"),
        ("masonry", "Masonry"),
        ("carousel", "Carousel")
    ], default="grid")

    class Meta:
        icon = "image"
        label = "Gallery Section"
        template = "blocks/gallery_block.html"


# ============================================================
#  TESTIMONIAL BLOCK
# ============================================================

class TestimonialItem(blocks.StructBlock):
    name = blocks.CharBlock(max_length=120)
    position = blocks.CharBlock(max_length=150, required=False)
    message = blocks.TextBlock()
    photo = ImageChooserBlock(required=False)

    class Meta:
        icon = "user"
        label = "Testimonial Item"
        template = "blocks/testimonial_item.html"


class TestimonialBlock(blocks.StructBlock):
    section_header = SectionHeaderBlock(required=False)
    testimonials = blocks.ListBlock(TestimonialItem)
    layout = blocks.ChoiceBlock(choices=[
        ("grid", "Grid"),
        ("slider", "Slider")
    ], default="slider")

    class Meta:
        icon = "group"
        label = "Testimonials Section"
        template = "blocks/testimonial_block.html"


# ============================================================
#  PROGRAMS & COURSES BLOCK
# ============================================================

class ProgramItem(blocks.StructBlock):
    name = blocks.CharBlock(max_length=150)
    description = blocks.TextBlock()
    duration = blocks.CharBlock(max_length=100, required=False)
    level = blocks.CharBlock(max_length=100, required=False)
    image = ImageChooserBlock(required=False)
    prospectus = DocumentChooserBlock(required=False)

    class Meta:
        icon = "folder-open-1"
        label = "Program Item"
        template = "blocks/program_item.html"


class ProgramListBlock(blocks.StructBlock):
    section_header = SectionHeaderBlock(required=False)
    programs = blocks.ListBlock(ProgramItem)
    layout = blocks.ChoiceBlock(choices=[
        ("grid", "Grid"),
        ("cards", "Cards Horizontal")
    ], default="grid")

    class Meta:
        icon = "list-ul"
        label = "Program List"
        template = "blocks/program_list_block.html"


# ============================================================
#  ADMISSIONS BLOCK
# ============================================================

class StepItem(blocks.StructBlock):
    number = blocks.CharBlock(max_length=10)
    title = blocks.CharBlock(max_length=150)
    description = blocks.TextBlock()

    class Meta:
        icon = "pick"
        label = "Step Item"
        template = "blocks/step_item.html"


class StepsBlock(blocks.StructBlock):
    section_header = SectionHeaderBlock(required=False)
    steps = blocks.ListBlock(StepItem)

    class Meta:
        icon = "order"
        label = "Step-by-Step Guide"
        template = "blocks/steps_block.html"


# ============================================================
#  EVENTS BLOCK
# ============================================================

class EventItem(blocks.StructBlock):
    title = blocks.CharBlock(max_length=150)
    date = blocks.DateBlock()
    location = blocks.CharBlock(max_length=200)
    description = blocks.TextBlock(required=False)
    link = blocks.URLBlock(required=False)
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = "date"
        label = "Event Item"
        template = "blocks/event_item.html"


class EventBlock(blocks.StructBlock):
    section_header = SectionHeaderBlock(required=False)
    events = blocks.ListBlock(EventItem)

    class Meta:
        icon = "date"
        label = "Events Section"
        template = "blocks/event_block.html"


# ============================================================
#  NEWS BLOCK
# ============================================================

class NewsItem(blocks.StructBlock):
    title = blocks.CharBlock(max_length=150)
    date = blocks.DateBlock()
    summary = blocks.TextBlock()
    image = ImageChooserBlock(required=False)
    link = blocks.URLBlock()

    class Meta:
        icon = "doc-full-inverse"
        label = "News Item"
        template = "blocks/news_item.html"


class NewsBlock(blocks.StructBlock):
    section_header = SectionHeaderBlock(required=False)
    news = blocks.ListBlock(NewsItem)

    class Meta:
        icon = "doc-full"
        label = "News Section"
        template = "blocks/news_block.html"


# ============================================================
#  FACULTY BLOCK
# ============================================================

class FacultyItem(blocks.StructBlock):
    name = blocks.CharBlock(max_length=150)
    position = blocks.CharBlock(max_length=200)
    department = blocks.CharBlock(max_length=150, required=False)
    photo = ImageChooserBlock()
    bio = blocks.TextBlock(required=False)

    class Meta:
        icon = "user"
        label = "Faculty Item"
        template = "blocks/faculty_item.html"


class FacultyListBlock(blocks.StructBlock):
    section_header = SectionHeaderBlock(required=False)
    faculty = blocks.ListBlock(FacultyItem)
    layout = blocks.ChoiceBlock(choices=[
        ("grid", "Grid"),
        ("cards", "Cards with Cover")
    ], default="grid")

    class Meta:
        icon = "group"
        label = "Faculty Directory"
        template = "blocks/faculty_list_block.html"


# ============================================================
#  RESEARCH BLOCK
# ============================================================

class ResearchItem(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200)
    researcher = blocks.CharBlock(max_length=150)
    abstract = blocks.TextBlock()
    document = DocumentChooserBlock(required=False)

    class Meta:
        icon = "folder-open-inverse"
        label = "Research Item"
        template = "blocks/research_item.html"


class ResearchBlock(blocks.StructBlock):
    section_header = SectionHeaderBlock(required=False)
    researches = blocks.ListBlock(ResearchItem)

    class Meta:
        icon = "docs"
        label = "Research Section"
        template = "blocks/research_block.html"


# ============================================================
#  CONTACT BLOCKS
# ============================================================

class MapBlock(blocks.StructBlock):
    embed_code = blocks.TextBlock(help_text="Paste Google Maps iframe code.")

    class Meta:
        icon = "site"
        label = "Google Map"
        template = "blocks/map_block.html"


class ContactDetailsBlock(blocks.StructBlock):
    address = blocks.TextBlock()
    phone = blocks.CharBlock(max_length=50)
    email = blocks.EmailBlock()
    office_hours = blocks.TextBlock(required=False)

    class Meta:
        icon = "mail"
        label = "Contact Details"
        template = "blocks/contact_details_block.html"


class ContactFormBlock(blocks.StructBlock):
    success_message = blocks.CharBlock(default="Your message has been sent.")

    class Meta:
        icon = "form"
        label = "Contact Form"
        template = "blocks/contact_form_block.html"
