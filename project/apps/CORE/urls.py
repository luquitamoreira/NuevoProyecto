from django.urls import path
from .views import home

app_name="CORE"

urlpatterns = [
    path("", home,name='home'),
]
