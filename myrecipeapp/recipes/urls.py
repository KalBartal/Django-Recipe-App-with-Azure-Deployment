from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import index, recipe_list, recipe_detail, recipe_create, recipe_update, recipe_delete, recipe_list_ajax

urlpatterns = [
    path('', index, name='index'),
    path('recipes/', recipe_list, name='recipe_list'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipes/create/', recipe_create, name='recipe_create'),
    path('recipes/<int:pk>/update/', recipe_update, name='recipe_update'),
    path('recipes/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
    path('recipes/list-ajax/', recipe_list_ajax, name='recipe_list_ajax'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
