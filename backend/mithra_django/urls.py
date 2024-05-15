"""mithra_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from MithraApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login/',views.login,name="Login"),
    path('Signup/',views.signup,name="SignUp"),
    path('Signup/Files-upload/',views.upload_files,name="Upload Files"),
    path('create-ride/',views.create_ride,name="Create Ride"),
    path('create-ride/payment-picture/',views.payment_pic,name="Create ride payment pic"),
    path('verification/',views.verification,name="User verification"),
    path('accept-verification/',views.verification_accept,name="User verification accept"),
    path('reject-verification/',views.verification_reject,name="User verification reject"),
    path('search-carpool/',views.search_ride,name="Search carpool"),
    path('request-carpool/',views.request_carpool,name="Request carpool"),
    path('view-profile/',views.view_profile,name="View profile"),
    path('driver-id-save/',views.save_driver,name="save driver id"),
    path('review-rating/',views.review_rating,name="review rating"),
    path('get-requests/',views.get_carpool_requests,name="get requests"),
    path('search-product-delivery/',views.search_product_delivery,name="search product delivery"),
    path('request-product-delivery/',views.request_product_delivery,name="request product delivery"),
    path('forgot-password/',views.forget_password,name="forgot password"),
    path('search-request/',views.request,name="Requests"),
    path('accept-request/',views.accept_request,name="Accept Requests"),
    path('reject-request/',views.reject_request,name="Reject Requests"),
    path('get-status/',views.get_status,name="Get request status"),
    path('cancel-content/',views.cancel_content,name="Cancel content"),
    path('cancel/',views.cancel,name="Cancel"),
    path('admin-created-carpool/',views.admin_created_carpool,name="Admin Created Carpool"),
    path('my-profile/',views.edit_profile,name="Edit profile"),
    path('upload-edit/',views.edit_upload,name="Edit upload"),
    path('final-payment/',views.final_payment,name="Final Payment"),
    path('check-driver/',views.check_driver,name="Check Driver"),
    path('verification-dl/',views.verification_dl,name="User verification dl"),
    path('accept-verification-dl/',views.verification_accept_dl,name="User verification accept dl"),
    path('reject-verification-dl/',views.verification_reject_dl,name="User verification reject dl"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
