from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, ArticleCreate, ArticleUpdate, PostDelete, SearchList

urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', ArticleCreate.as_view(), name='create_article'),
   path('<int:pk>/edit/', ArticleUpdate.as_view(), name='edit_article'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', SearchList.as_view(), name='search_publications'),
]
