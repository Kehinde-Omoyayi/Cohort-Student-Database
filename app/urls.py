from django.urls import path
from . import views

urlpatterns =[
    path('home/', views.home_page, name='Home_page'),
    path('student/', views.student_page.as_view(), name='student_page'),
    path('profile/', views.profile_page.as_view(), name='profile_page'),
    path('register/', views.register_page, name='register_page'),
    path('login/', views.student_login, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('account/', views.student_create_account, name='account_page'),
]