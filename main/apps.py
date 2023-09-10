from django.apps import AppConfig


class SocialConfig(AppConfig):
    name = 'main'
    
def ready (self):
    import main.signais
