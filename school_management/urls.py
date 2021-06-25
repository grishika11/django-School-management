"""school_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import school.views
#from django.contrib.staticfiles.urls import static
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',school.views.Home,name='home'),
    path('contact',school.views.Contact,name='contact'),
    path('about',school.views.About,name='about'),
    path('gallery',school.views.Gallery,name='gallery'),
    path('admin_login',school.views.Adminlog, name='admin_login'),
    path('logout',school.views.Logout, name='logout'),
    path('upload',school.views.Upload, name='upload'),
    path('admission',school.views.Admission, name='admission'),
    path('career',school.views.Career, name='career'),
    path('career_view',school.views.Career_view, name='career_view'),
    path('student_view',school.views.Student_view, name='student_view'),
    path('deleteit/<str:pk>/',school.views.delete_data_career,name='deleteit'),
    path('delete_admission/<int:id>',school.views.delete_data_admission,name='deletedata1'),
    path('export_csv',school.views.export_csv,name='export-csv'),
    path('export_excel',school.views.export_excel,name='export-excel'),
    path('delete_image/<int:id>',school.views.delete_img,name='deletedata2'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

