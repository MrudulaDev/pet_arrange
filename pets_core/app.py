from django.apps import AppConfig

class PetsCoreAppConfig(AppConfig):
    name = "pets_core"

    def ready(self):
        from pets_core import signals # pylint: disable=unused-variable
