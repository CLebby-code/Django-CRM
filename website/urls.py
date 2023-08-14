from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    # path('login/', views.login_user, name='login'),
    path("logout/", views.logout_user, name="logout"),
    path("register_user/", views.register_user, name="register_user"),
    path("customer_record/<int:pk>", views.customer_record, name="customer_record"),
    path("customer_list/", views.customer_list, name="customer_list"),
    path("delete_customer/<int:pk>", views.delete_customer, name="delete_customer"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("add_company/", views.add_company, name="add_company"),
    path(
        "update_customer/<int:pk>",
        views.update_customer,
        name="update_customer",
    ),
    path("company_list/", views.company_list, name="company_list"),
    path(
        "company_details/<int:pk>",
        views.company_details,
        name="company_details",
    ),
    path("update_company/<int:pk>", views.update_company, name="update_company"),
    path("delete_company/<int:pk>", views.delete_company, name="delete_company"),
    path("add_note/", views.add_note, name="add_note"),
]
