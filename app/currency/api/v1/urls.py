from rest_framework.routers import DefaultRouter

from app.currency.api.v1.views import (
RateViewSet, SourceViewSet, ContactUsViewSet
)

router = DefaultRouter(trailing_slash=False)
router.register('rates/', RateViewSet, basename='rates')
router.register('source/', SourceViewSet, basename='source')
router.register('contactus/', ContactUsViewSet, basename='contactus')

app_name = 'currency_api'

urlpatterns = [
] + router.urls
