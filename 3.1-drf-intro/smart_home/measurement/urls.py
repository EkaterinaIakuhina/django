from django.urls import path

from measurement.views import EachSensorView, MeasurementView, SensorsView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', EachSensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]