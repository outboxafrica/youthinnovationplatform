from django import template
import ast

register = template.Library()


@register.filter
def sanitise_image(value):
    return "/" + value


@register.filter
def listify(value):
    if (value):
        listified = ast.literal_eval(value)
        return " | ".join(listified)
    return value


@register.filter
def listifyNL(value):
    if (value):
        listified = ast.literal_eval(value)
        return " <br> ".join(listified)
    return value


@register.filter
def status(value):
    try:
        print int(value)
        values = ["Ideation", "Commitment", "Concepting", "Validation", "Scaling", "Established"]
        return values[int(value) - 1]
    except Exception, e:
        print value

    return value


@register.filter
def listChoice(value):
    value = value.replace('[', '').replace(']', '')
    value = value.split(', ')
    listy = [i.replace("u'", "") for i in value]
    clean_list = [i[:-1] for i in listy]
    return clean_list


@register.filter
def listSector(value):
    value = value.replace('[', '').replace(']', '')
    value = value.split(', ')
    listy = [i.replace("u'", "") for i in value]
    clean_list = [i[:-1] for i in listy]
    sectors = ", ".join(clean_list)
    return sectors.title()

@register.filter
def listOtherSector(value):
    value = value.replace('[', '').replace(']', '')
    value = value.split(', ')
    listy = [i.replace("u'", "") for i in value]
    clean_list = [i for i in listy]
    sectors = ", ".join(clean_list)
    return sectors.title()


@register.filter()
def currency(value):
    return "UGX " + str(value)


@register.filter()
def split_by_comma(value):
    return value.split(" ")