"""HelloWorld2 URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('helloapp.urls')),
    path('todo/', include('todo.urls')),
    path('photo/', include('photo_upload.urls')),
    path('poll/', include('vote.urls'))
    # static('/media', BASE_DIR/upload/photos) <- 아래 개념 설명용
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # 위의 urlpatterns와 성격이 달라서 따로 추가해줌