from django.urls import include, path
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views


router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)

urlpatterns = router.urls
