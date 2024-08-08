import os

from bb.files.enums import FileUploadStorage, FileUploadStrategy
from config.env import BASE_DIR, env, env_to_enum

FILE_UPLOAD_STRATEGY = env_to_enum(FileUploadStrategy, env("FILE_UPLOAD_STRATEGY", default="standard"))
FILE_UPLOAD_STORAGE = env_to_enum(FileUploadStorage, env("FILE_UPLOAD_STORAGE", default="local"))

FILE_MAX_SIZE = env.int("FILE_MAX_SIZE", default=10485760)  # 10 MiB

# TODO STACK: Replace local storage with with Azurite to more closely match production environment
# https://django-storages.readthedocs.io/en/latest/backends/azure.html#using-with-azurite-previously-azure-storage-emulator
if FILE_UPLOAD_STORAGE == FileUploadStorage.LOCAL:
    MEDIA_ROOT_NAME = "media"
    MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_ROOT_NAME)
    MEDIA_URL = f"/{MEDIA_ROOT_NAME}/"

if FILE_UPLOAD_STORAGE == FILE_UPLOAD_STORAGE.AZURE:
    # TODO STACK: Add Azure storage backend
    # Using django-storages
    # https://django-storages.readthedocs.io/en/latest/backends/azure.html
    ...
