
from django.urls import path

from .views import todoview,todoaddview,tododelete

urlpatterns = [
    path('', todoview,name='todo'),
    path( 'todoadd', todoaddview,name='todoadd'),
    path('delete/<todo_id>',tododelete,name='delete')
]
