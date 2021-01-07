from django import template

# Custom template filters for dealing with nested dictionaries and tree views

register = template.Library()

@register.filter
def make_path_pretty(value):
    """
    Shows the filepath in a JSON to the user, with whitespace instead of a double underscore.
    """
    value = value.replace('__',' ')
    value = value.replace('//',' // ')
    return(value)

@register.filter
def keyvalue(dictionary,key):
    """
    Retrieve dictionary key value
    """
    return dictionary.get(key)

@register.filter
def replace_whitespace(value):
    """
    Replaces each whitespace character with a double underscore
    """
    return value.replace(' ','__')

@register.filter
def add_to_path(value,arg):
    """
    Adds another item to the current path
    """
    return value + '//' + arg.replace(' ','__')

@register.filter
def add_ref(value):
    """
    Adds a # in front of a string (use this to make references to html elements)
    """
    return '#' + value

@register.filter
def add_tab(value):
    """
    Adds _tab onto the end of a string (use this to help distinguish between tabs and tab content)
    """
    return value + '_tab'

@register.filter
def add_body(value):
    """
    Adds _body onto the end of a string (use this to help distinguish between cards and card content)
    """
    return value + '_body'

@register.simple_tag
def get_rownames(x):
    """
    Gets row names from a dictionary representing a table
    """
    rownames = list(x.keys())
    return rownames

@register.simple_tag
def get_colnames(x):
    """
    Gets column names from dictionary representing a table
    """
    k = list(x.keys())[0]
    colnames = list(x[k].keys())
    return colnames

@register.simple_tag
def bound_field(form, fieldname):
    """ Returns bound field """
    return form.__getitem__(fieldname)
