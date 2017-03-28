import re
from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cloudinary.uploader import upload, upload_resource
from cloudinary.forms import CloudinaryFileField
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryResource
from cloudinary.models import UploadedFile

CLOUDINARY_FIELD_DB_RE = r'(?:(?P<resource_type>image|raw|video)/(?P<type>upload|private|authenticated)/)?(?:v(?P<version>\d+)/)?(?P<public_id>.*?)(\.(?P<format>[^.]+))?$'


def handle_uploads(file):
    response = upload(file, resource_type='raw')
    return response['secure_url']


# class CustomCloudinaryFileField(CloudinaryFileField):
#     def __init__(self, options=None, autosave=True, *args, **kwargs):
#         CloudinaryFileField.__init__(self, options=None, autosave=True, *args, **kwargs)
#         super(CustomCloudinaryFileField, self).__init__(*args, **kwargs)
#
#     def change_python(self, value):
#         """Upload and convert to CloudinaryResource"""
#         if not value:
#             return None
#         if self.autosave:
#             return upload(value, resource_type='raw')
#         else:
#             return value
#
#     def to_python(self, value):
#         """Upload and convert to CloudinaryResource"""
#         value = self.change_python(value)
#         if not value:
#             return None
#         if self.autosave:
#             return upload(value, resource_type='raw', **self.options)
#         else:
#             return value


class CustomCloudinaryFileField(forms.FileField):
    my_default_error_messages = {
        'required': _(u"No file selected!")
    }
    default_error_messages = forms.FileField.default_error_messages.copy()
    default_error_messages.update(my_default_error_messages)

    def __init__(self, autosave=True, *args, **kwargs):
        self.autosave = autosave
        super(CustomCloudinaryFileField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        """Upload and convert to CloudinaryResource"""
        value = super(CustomCloudinaryFileField, self).to_python(value)
        print "value", value
        if not value:
            return None
        if self.autosave:
            return upload(value, resource_type='raw')
        else:
            return value


class CloudinaryField(models.Field):
    description = "A resource stored in Cloudinary"

    def __init__(self, *args, **kwargs):
        options = {'max_length': 255}
        self.default_form_class = kwargs.pop("default_form_class", CloudinaryFileField)
        options.update(kwargs)
        self.type = options.pop("type", "upload")
        self.resource_type = options.pop("resource_type", "image")
        super(CloudinaryField, self).__init__(*args, **options)

    def get_internal_type(self):
        return 'CharField'

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)

    def parse_cloudinary_resource(self, value):
        m = re.match(CLOUDINARY_FIELD_DB_RE, value)
        resource_type = m.group('resource_type') or self.resource_type
        upload_type = m.group('type') or self.type
        return CloudinaryResource(
            type=upload_type,
            resource_type=resource_type,
            version=m.group('version'),
            public_id=m.group('public_id'),
            format=m.group('format')
        )

    def from_db_value(self, value, expression, connection, context):
        if value is None:
            return value
        return self.parse_cloudinary_resource(value)

    def to_python(self, value):
        if isinstance(value, CloudinaryResource):
            return value
        elif isinstance(value, UploadedFile):
            return value
        elif value is None:
            return value
        else:
            return self.parse_cloudinary_resource(value)

    def upload_options_with_filename(self, model_instance, filename):
        return self.upload_options(model_instance)

    def upload_options(self, model_instance):
        return {}

    def pre_save(self, model_instance, add):
        value = super(CloudinaryField, self).pre_save(model_instance, add)
        if isinstance(value, UploadedFile):
            options = {"type": self.type, "resource_type": 'raw'}
            options.update(self.upload_options_with_filename(model_instance, value.name))
            instance_value = upload_resource(value, **options)
            setattr(model_instance, self.attname, instance_value)
            return self.get_prep_value(instance_value)
        else:
            return value

    def get_prep_value(self, value):
        if not value:
            return self.get_default()
        if isinstance(value, CloudinaryResource):
            return value.get_prep_value()
        else:
            return value

    def formfield(self, **kwargs):
        options = {"type": self.type, "resource_type": self.resource_type}
        options.update(kwargs.pop('options', {}))
        defaults = {'form_class': self.default_form_class, 'options': options, 'autosave': False}
        defaults.update(kwargs)
        return super(CloudinaryField, self).formfield(**defaults)
