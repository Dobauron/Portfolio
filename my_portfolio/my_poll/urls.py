from django.urls import path
from .views import polls_list

app_name = "my_polls"


urlpatterns = (
    path('poll/', polls_list),
)
