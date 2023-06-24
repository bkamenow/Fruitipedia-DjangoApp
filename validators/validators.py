from django.core.exceptions import ValidationError


def first_name_length_char_validator(value):
    if len(value) < 2 or len(value) > 25:
        raise ValidationError('First name must be between 2 and 25 chars!')


def last_name_length_char_validator(value):
    if len(value) < 1 or len(value) > 35:
        raise ValidationError('Last name must be between 1 and 35 chars!')


def name_start_with_letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError('Your name must start with a letter!')


def password_length_validator(value):
    if len(value) < 8 or len(value) > 20:
        raise ValidationError('Password must be between 8 and 20 chars!')


def fruit_name_validator(value):
    if len(value) < 2 or len(value) > 30:
        raise ValidationError('Fruit name must be between 2 and 30 chars!')


def fruit_name_contain_only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')
