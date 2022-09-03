from django.urls import path
from .views import student_onboarding

urlpatterns = [
	path('new_onboard/', views.student_onboarding),
	# path('candidate_details', views.)
]