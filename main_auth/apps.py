from django.apps import AppConfig


class MainAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'main_auth'

    def ready(self):
        import main_auth.signals