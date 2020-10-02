from django.apps import AppConfig


class BookstoreConfig(AppConfig):
    name = 'bookstore'

    def ready(self):
       import bookstore.signals
