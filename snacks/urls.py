from django.urls import path
from .views import SnackDetailView, SnackListView , SnackCreateView , SnackUpdateView , SnackDeleteView
urlpatterns = [
    path('', SnackListView.as_view(), name='snacks'),
    path('<pk>',SnackDetailView.as_view(), name="snack_details"),
    path('create/', SnackCreateView.as_view(), name= 'create_snack'),
    path('update/<pk>',SnackUpdateView.as_view(), name= 'update_snack'),
    path('delete/<pk>',SnackDeleteView.as_view(), name= 'delete_snack')

]