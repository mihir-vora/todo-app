from django.urls import path
from .views import (
	index,
	edit,
	delete,
)
from . import views


urlpatterns = [
	path('', index, name="blog-index"),
	path('edit/<int:pk>/', edit, name="edit"),
	path('delete/<int:pk>/', delete, name="delete"),
]