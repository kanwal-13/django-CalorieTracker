from django.apps import AppConfig


class CalorieTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calorie__tracker'

    def ready(self):
        import calorie__tracker.signals