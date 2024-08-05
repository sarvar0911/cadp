from django.apps import AppConfig

class CadpAboutConfig(AppConfig):
    name = 'cadp_about'

    def ready(self):
        from config import translation
