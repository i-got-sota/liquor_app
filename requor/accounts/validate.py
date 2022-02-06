from django.core.exceptions import ValidationError

def validate_age(value):
    value = int(value)
    adult_age = 20

    if value < adult_age:
        raise ValidationError('このアプリは未成年の方はご利用いただけません。')