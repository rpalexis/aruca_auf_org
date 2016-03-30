from django.db import models

def object_fields (instance, ignore = []):
    fields = []
    headers = []

    for field in instance._meta.fields:
        name = field.verbose_name
        if len(name.strip()) == 0:
            name = field.name
        if field.name not in ignore:
            fields.append (field.name)
            headers.append (name)

    return (fields, headers)

def object_values (instance, fields, choice_values = True):
    sorted_values = []
    values = {}

    for field in instance._meta.fields:
        if choice_values:
            value = instance._get_FIELD_display (field)
        else:
            value = getattr (instance, field.name)
        if value is None:
            value = u""
        if hasattr (value, "encode"):
            value = value.encode("utf-8")
        else:
            value = str(value)
        values[field.name] = value


    for field in fields:
        sorted_values.append (values[field])

    return sorted_values

setattr (models.Model, 'object_fields', object_fields)
setattr (models.Model, 'object_values', object_values)
