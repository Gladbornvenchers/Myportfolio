from django.urls import path

from . import views
from .views import portfolio_home, contact_page



urlpatterns = [
    path("", portfolio_home, name="portfolio_home"),
    path("contact/", contact_page, name = "contact_page"),
]
