from django.urls import path
from .views import post_detail, post_list, PostListView, TaggedListView

urlpatterns = (
    path('blog/<slug:slug>/', TaggedListView.as_view(), name='post_list_by_tag'),
    path('blog/', PostListView.as_view(), name='post_list'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail,
         name='post_detail'),
)
