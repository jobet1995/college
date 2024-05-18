from django.urls import path
from . import views

urlpatterns = [
    path('enrollment/<enrollment_form>/<enrollment_id>',
         views.EnrollmentInfo.as_view(), name='enrollment_forms'),
    path('info', views.EnrollmentInfo.as_view(), name='info'),
    path('enrollment/create', views.CreateEnrollment.as_view())
]
