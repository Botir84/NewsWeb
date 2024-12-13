from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('category/<str:category_name>/', views.category, name='category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('our-team/', views.our_team, name='our_team'),
    path('create_article/', views.create_article, name='create_article'),
    path('delete_article/', views.delete_article, name='delete_article')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)