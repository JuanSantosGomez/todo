from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.index, name="list"),
    path('update_task/<str:pk>/',views.updateTask,name="update_task"),
    path('delete_task/<str:pk>/',views.deleteTask,name="delete_task")


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)