
from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('buy/<str:category>/',views.shop),
    path('buy-cat/<str:category>/',views.shop),
    path('enquiry/<int:id>/',views.EnquiryPage),
    path('customized-enquiry/',views.CustomizedEnquiryPage)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
