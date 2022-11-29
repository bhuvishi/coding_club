"""coding_club URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from api.views import StudentList, StudentDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', StudentList.as_view()),
    path('api/students/{id}', StudentDetail.as_view()),
    path('web/', include('web.urls')),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)
