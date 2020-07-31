from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "what_can_i_cook.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import what_can_i_cook.users.signals  # noqa F401
        except ImportError:
            pass
