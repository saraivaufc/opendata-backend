import os

from django.conf import settings

if not settings.PRODUCTION:
    from django.core.files.storage import FileSystemStorage


    class OverwriteStorage(FileSystemStorage):
        """Subclass of FileSystemStorage which clobbers existing file"""

        def __init__(self, *args, **kwargs):
            """defaults to self.MEDIA_ROOT if location is not passed in"""
            self.location = kwargs.pop('location', settings.MEDIA_ROOT)
            super(OverwriteStorage, self).__init__(*args, **kwargs)

        def get_available_name(self, name, max_length=None):
            """deletes pre-existing file with same name
            preventing filename mangling"""
            if self.exists(name):
                os.remove(os.path.join(self.location, name))
            return name


    class StaticStorage(OverwriteStorage):
        pass


    class PublicMediaStorage(OverwriteStorage):
        pass


    class PrivateMediaStorage(OverwriteStorage):
        pass


else:
    from storages.backends.gcloud import GoogleCloudStorage


    class StaticStorage(GoogleCloudStorage):

        def get_default_settings(self):
            default_settings = super().get_default_settings()
            default_settings['location'] = settings.GS_STATIC_LOCATION
            default_settings['default_acl'] = 'publicRead'
            return default_settings


    class PublicMediaStorage(GoogleCloudStorage):

        def get_default_settings(self):
            default_settings = super().get_default_settings()
            default_settings['location'] = settings.GS_PUBLIC_MEDIA_LOCATION
            default_settings['file_overwrite'] = True
            default_settings['default_acl'] = 'publicRead'
            return default_settings


    class PrivateMediaStorage(GoogleCloudStorage):

        def get_default_settings(self):
            default_settings = super().get_default_settings()
            default_settings['location'] = settings.GS_PRIVATE_MEDIA_LOCATION
            default_settings['file_overwrite'] = True
            default_settings['default_acl'] = 'projectPrivate'
            return default_settings
