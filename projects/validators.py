import os

from django.core.exceptions import ValidationError


def validate_img(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg', '.jpg', '.png', '.gif']

    if ext not in valid_extensions:
        raise ValidationError(u'File not supported!')


def validate_doc(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx', '.xls',
                        'xlsx', '.txt', '.csv', ]

    if ext not in valid_extensions:
        raise ValidationError(u'File not supported!')


def validate_xls(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xls', 'xlsx', '.csv', '.ods',]

    if ext not in valid_extensions:
        raise ValidationError(u'Only Excel spreadsheets are supported')
