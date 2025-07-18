from django.apps import AppConfig


class SearchtoolConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "searchtool"

    def ready(self):
        # Import signals to register them
        import searchtool.signals  # noqa
