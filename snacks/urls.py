from django.urls import path
from .views import SnackDetailView, SnackListView
urlpatterns = [
    path('', SnackListView.as_view(), name='snacks'),
    path('<pk>',SnackDetailView.as_view(), name="snack_details")
]