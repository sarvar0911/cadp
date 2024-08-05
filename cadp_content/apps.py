from django.apps import AppConfig

class CadpContentConfig(AppConfig):
    name = 'cadp_content'

    def ready(self):
        from config import translation
