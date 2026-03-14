from django.urls import path
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns= [
    path('student/',views.api_student.as_view(),name='student_api'),
    path('profile/',views.api_student_ind.as_view(), name='student_ind_api'),

    #for authentication
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #for docunmentation
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),    
]
