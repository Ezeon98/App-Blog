from django.urls import path
from .views import BlogListView, BlogCreateView

app_name = "blog"

urlpatterns = [
    path('inicio/', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),

]