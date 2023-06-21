from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    # path('login/', views.login_user, name='login'),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("record/<int:pk>", views.customer_record, name="record"),
    path("delete_record/<int:pk>", views.delete_record, name="delete_record"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("add_company/", views.add_company, name="add_company"),
    path("update_customer/<int:pk>", views.update_customer, name="update_customer"),  # noqa: E501
    path("company_info/<int:pk>", views.company_info, name="company_info"),
    path("update_company/", views.update_company, name="update_company"),
    path("delete_company/", views.delete_company, name="delete_company"),
]
