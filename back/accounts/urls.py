from django.urls import path

from . import views


app_name = 'accounts'

urlpatterns = [
    path('<int:user_id>/', views.UserDetailView.as_view()),
]