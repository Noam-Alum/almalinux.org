from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscribe/thank-you/', views.subscribe_post, name='subscribe_post'),
    path('p/<slug:slug>/', views.content_page, name='page'),
    path('blog/', views.blog_index, name='blog_index'),
    path('blog/page/<int:page_num>/', views.blog_index, name='blog_index_page'),
    path('blog/<slug:slug>/', views.blog_post, name='blog_post'),
]