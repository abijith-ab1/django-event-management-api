from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserListCreateView, UserDetailView, EventListCreateView, EventDetailView,
    RegistrationListCreateView, RegistrationDetailView, UserReportView, EventReportView, CountView
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('registrations/', RegistrationListCreateView.as_view(), name='registration-list-create'),
    path('registrations/<int:pk>/', RegistrationDetailView.as_view(), name='registration-detail'),
    path('reports/users/', UserReportView.as_view(), name='user-report'),
    path('reports/events/', EventReportView.as_view(), name='event-report'),
    path('count/', CountView.as_view(), name='count-view'),
]
