from django.urls import path
from .views import *

urlpatterns = [
    path('blog', BlogListView.as_view(), name="BlogListView"),
    path('blog/CreatePost', CreatePostView.as_view(), name="CreatePostView"),
    path('blog/PostDetail/<int:pk>', PostDetailView.as_view(), name="PostDetailView"),
    path('blog/UpdatePost/<int:pk>', UpdatePostView.as_view(), name="UpdatePostView"),
    path('blog/<int:pk>/DeletePost', DeletePostView.as_view(), name="DeletePostView"),
    path('blog/CreateCategory', CreateCategoryView.as_view(), name="CreateCategoryView"),
    path('blog/category/<str:continents>', CategoryView, name='CategoryView'),
    path('blog/LikePost/<int:pk>', LikePost, name='LikePost'),
    path('blog/search/', search, name='search'),
]