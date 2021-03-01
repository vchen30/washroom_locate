# mysite/wee/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('post/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('washroom/<int:pk>', views.washroom_detail, name='washroom_detail'),
    path('review/<int:pk>', views.review_washroom, name='review_washroom'),
    path('review/<int:pk>', views.washroom_detail, name='review_was_posted'),
]
