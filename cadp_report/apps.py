from django.apps import AppConfig

class CadpReportConfig(AppConfig):
    name = 'cadp_report'

    def ready(self):
        from config import translation
