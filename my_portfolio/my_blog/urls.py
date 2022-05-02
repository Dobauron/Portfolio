from django.urls import path
from .views import post_detail, post_list
urlpatterns = (
    path('tag/<slug:tag_slug>/', post_list, name = 'post_list_by_tag'),
    path('blog/', post_list, name='post_list'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail,
         name= 'post_detail'),
)