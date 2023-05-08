from django.apps import AppConfig


class BuildersConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'builders'

    def ready(self):
        import builders.signals
