from . import views


def register(router):
    router.register(r'entries', views.Entries)
