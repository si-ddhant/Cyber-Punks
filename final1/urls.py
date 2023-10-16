from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from . import views
from .views import RecordCountView, MeanSalaryView, MedianSalaryView, TableViewSet

# Create a router for your API views
router = DefaultRouter()
# Replace with your model and viewset
router.register(r'Table', views.TableViewSet)


def homepage(Request):
    return HttpResponse("Hello MotherFucker!!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/record-count/', RecordCountView.as_view(), name='record-count'),
    path('api/mean-salary/', MeanSalaryView.as_view(), name='mean-salary'),
    path('api/median-salary/', MedianSalaryView.as_view(), name='median-salary'),

    # Include your API endpoints here
    # Add more URL patterns as needed for other views
]

# Additional URL patterns can be added for non-API views
