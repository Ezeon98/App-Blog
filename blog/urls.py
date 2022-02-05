from django.urls import path
from .views import BlogListView, BlogCreateView, DetailPostView, BlogUpdateView

app_name = "blog"

urlpatterns = [
    path('inicio/', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/', DetailPostView.as_view(), name='detail'), ## <int:pk> hace referencia al ID del modelo
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='update')
]