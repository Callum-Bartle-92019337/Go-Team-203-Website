from django.urls import path

from . import views

# adds the main url patterns to the urls so you can access each view
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('History/', views.history, name='history'),
    path('Contact/', views.contact, name='contact'),
    path('PrivacyPolicy/', views.privacyPolicy, name='privacyPolicy'),
    path('TermsOfService/', views.termsOfService, name='termsOfService'),
    path('reviews/new', views.NewReviewView.as_view(), name='review_new'),
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/', views.ReviewsListViewStandard.as_view(), name='reviews_list_strd'),
    path('myreviews/', views.ReviewsListViewAuthent.as_view(), name='reviews_list_auth'),
    path('reviews/food', views.ReviewsListViewFood.as_view(), name='reviews_list_food'),
    path('reviews/activities', views.ReviewsListViewActivities.as_view(), name='reviews_list_activities'),
    path('reviews/accommodation', views.ReviewsListViewAccommodation.as_view(), name='reviews_list_accommodation'),

]
