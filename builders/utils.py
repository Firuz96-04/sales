import io
import os
from datetime import date
import uuid

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from pathlib import Path
from datetime import date


def get_cur_date():
    today = date.today()
    return today


# def upload_to(instance, filename):
#     extension = filename.split('.')[-1]
#     new_filename = '{}.{}'.format(uuid.uuid4(), extension)
#     return 'images/{}'.format(new_filename)

def upload_path(prefix, instance, filename):
    ext = filename.split('.')[-1]
    today = date.today().strftime('%Y/%m/%d')
    filename = f'{uuid.uuid4().hex[:16]}.webp'
    return '{prefix}/{today}/{filename}'.format(
        prefix=prefix,
        today=today,
        filename=filename)


def upload_builder_logo(instance, filename):
    return upload_path('builder/logo', instance, filename)


def upload_resident_banner(instance, filename):
    return upload_path('resident/banner', instance, filename)


def upload_manager_photo(instance, filename):
    return upload_path('manager/photo', instance, filename)


def upload_builder_license(instance, filename):
    return upload_path('builder/license', instance, filename)


def upload_block_floor(instance, filename):
    return upload_path('builder/floor', instance, filename)


def upload_block_apartment(instance, filename):
    return upload_path('builder/apartment', instance, filename)


@deconstructible
class ImageValidator:
    def __init__(self, allowed_extensions=('png', 'jpg', 'jpeg', 'webp')):
        self.allowed_extensions = allowed_extensions

    def __call__(self, value):
        if value:
            filename = value.name.lower()
            extension = filename.rsplit('.', 1)[-1]
            if extension not in self.allowed_extensions:
                raise ValidationError('Only {} files are supported'.format(', '.join(self.allowed_extensions)))
            try:
                with Image.open(value.file) as img:
                    pass
            except IOError:
                raise ValidationError('Not a valid image file')

# def convert_to_webp(f_object: InMemoryUploadedFile):
#     suffix = Path(f_object._name).suffix
#     if suffix == ".webp":
#         return f_object._name, f_object
#
#     new_file_name = str(Path(f_object._name).with_suffix('.webp'))
#     image = Image.open(f_object.file)
#     thumb_io = io.BytesIO()
#     image.save(thumb_io, 'webp', optimize=True, quality=95)
#
#     new_f_object = InMemoryUploadedFile(
#         thumb_io,
#         f_object.field_name,
#         new_file_name,
#         f_object.content_type,
#         f_object.size,
#         f_object.charset,
#         f_object.content_type_extra
#     )
#
#     return new_file_name, new_f_object

# def validator_image_size(value):
#     # print(dir(value))
#     print(value.size, 'size')
#     return  value