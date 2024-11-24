from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """
    Multiplica un valor por un argumento.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''
