from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('History/', views.history, name='history'),
    path('Contact/', views.contact, name='contact'),
    path('PrivacyPolicy/', views.privacyPolicy, name='privacyPolicy'),
    path('TermsOfService/', views.termsOfService, name='termsOfService'),
    path('TheMaking/', views.theMaking, name='theMaking'),
    path('reviews/new', views.NewReviewView.as_view(), name='review_new'),
    path('review/<int:pk>', views.ReviewDetailView.as_view(), name='review_detail'),
    path('reviews/', views.ReviewsListViewStandard.as_view(), name='reviews_list_strd'),
    path('myreviews/', views.ReviewsListViewAuthent.as_view(), name='reviews_list_auth'),

]
