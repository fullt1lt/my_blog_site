"""
URL configuration for blog_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from my_site.views import (article_delete, article_update, 
                            contacts, create, deactivate, home, article, login, logout, profile, register, set_password, set_userdata,test,about,article_comment, 
                            topics, topics_add, topics_remove, topics_subscribe, topics_unsubscribe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about),
    path('', home, name='index'),
    path('article/<int:article_id>/', article, name='article'),
    path('article/<int:article_id>/comment/', article_comment, name='article_comment'),
    path('create/', create),
    path('article/<int:article_id>/update/', article_update, name='article_update'),
    path('article/<int:article_id>/delete/', article_delete, name='article_delete'),
    path('topics/', topics),
    path('topics/<int:topic_id>/add/', topics_add, name='topics_add'),
    path('topics/<int:topic_id>/remove/', topics_remove, name='topics_romove'),
    path('topics/<int:topic_id>/subscribe/', topics_subscribe, name='topics_subscribe'),
    path('topics/<int:topic_id>/unsubscribe/', topics_unsubscribe, name='topics_unsubscribe'),
    path('profile/<str:username>/', profile, name='profile'),
    path('set-password/', set_password, name='set_password'),
    path('set-userdata/', set_userdata, name='set_userdata'),
    path('deactivate/', deactivate, name='deactivate'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
    
    path('test/', test, name='test'),
    path('contacts/', contacts, name='contacts')
]
