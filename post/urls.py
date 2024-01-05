from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.post),
    path('get-featured-posts/', views.get_featured_posts),
    path('get-most-viewed-posts/', views.get_most_viewed_posts),
    path('get-top-authors/', views.get_top_users_with_max_post_views),
    path('get-all-categories/', views.get_all_categories),
    path('todays_update/', views.todays_update),
    path('insta_posts/', views.get_all_insta_posts),
    path('get-all-tags/', views.get_all_tags),



    # path('get-recent-posts/', views.get_recent_posts),


]
