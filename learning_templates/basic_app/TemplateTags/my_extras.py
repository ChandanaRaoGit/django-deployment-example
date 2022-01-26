from django import template

register = template.Library()
@register.filter(name='cut') #calling inbuilt decorator.
def cut(value,arg):
    """
    THIS CUTS OUT ALL VALUES OF "arg" FROM THE STRING!
    """
    return value.replace(arg,'')

# register.filter('cut',cut) # 1st arg is the variable we use when we call a function. 2nd arg is passing the actual function.
