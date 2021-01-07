from django.core.exceptions import ValidationError
import parameters.json_helper_functions as jf

def validate_integer_list(value):
    # Validates form input for lists, which are rendered in forms as a CharField (input will be a string)
    # value should be a comma separated list of integers, represented as a string, which may also be enclosed in square brackets (but don't have to be)

    try:
        jf.string_to_integer_list(value)
    except:
        raise ValidationError("Invalid input. Please enter a comma separated list of integers enclosed by square brackets")
