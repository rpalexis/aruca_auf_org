from django import template
register = template.Library()


@register.filter(name="add_css_classes")
def add_css_classes(field,css):
    return field.as_widget(attrs ={"class":css})

@register.filter(name="add_placeholder")
def add_css_classes(field,css):
    return field.as_widget(attrs ={"placeholder":css})
