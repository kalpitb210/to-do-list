from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.add_new_todo, name='submit'),
    path('safe_edit/<int:pk>', views.safe_edit, name='safe_edit'),
    path('list', views.all_todos, name='todos_list'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('sort', views.sort, name='sort'),
    path('search', views.search, name='search'),
    path('edit/<int:pk>', views.edit, name='edit')
]
