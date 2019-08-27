import logging

from django.contrib.auth import logout as django_logout
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import generic
from .models import Review
from .forms import SignUpForm, ReviewNewForm

# Registers the log file
log = logging.getLogger(__name__)

# Registers the company name to pass to each page later
companyName = "Culture Master"


# Home page view
def home(request):
    # Gets the most recent review to pass to the homepage
    queryset1 = Review.objects.order_by('-posted')[:1]

    # Stores the page title and description to pass to the template
    meta = {
        'title': 'Home',
        'companyName': companyName,
        'review_list': queryset1,

        'description': companyName + ' home page where you can see a quick rundown of the page and its features'
    }
    return render(request, 'home/home.html', meta)


# About view
def history(request):
    meta = {
        'title': 'About',
        'description': companyName + ' a short history of the app and the prosess that created it'
    }
    return render(request, 'home/about_us.html', meta)


# Contact view
def contact(request):
    meta = {
        'title': 'Contact Us',
        'description': companyName + ' contact page, the form used to submit reviews and bug reports'
    }
    return render(request, 'home/contact_us.html', meta)


# Privacy statement view
def privacyPolicy(request):
    meta = {
        'title': 'Privacy Policy',
        'description': companyName + ' privacy policy page updated 21st august 2018'
    }
    return render(request, 'home/privacy_policy.html', meta)


# Terms of service view
def termsOfService(request):
    meta = {
        'title': 'Terms of Service',
        'description': companyName + ' terms of service page updated august 21st 2018'
    }
    return render(request, 'home/terms_of_service.html', meta)


# Logout view
def logout(request):
    meta = {
        'title': 'Logout',
        'description': companyName + ' Logout'
    }
    log.warning(request.user.username + ' Logged out')
    django_logout(request)
    return render(request, 'registration/logged_out.html', meta)


# Password reset view
def reset_request(request):
    meta = {
        'title': 'Password Reset',
        'description': companyName + ' Password Reset'
    }
    log.warning('Password change request made')
    return render(request, 'registration/password_reset_form.html', meta)

# Signup view / Create user
def signup(request):
    meta = {
        'title': 'Signup',
        'description': companyName + ' Signup'
    }

    # if we get a post request with the form save the user as a new user
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'meta': meta})

# The view where you post a new review if loged in
class NewReviewView(generic.FormView):
    template_name = 'home/new_review.html'
    form_class = ReviewNewForm
    success_url = '/home'

    def form_valid(self, form):

        # If the review form is valid save it to the database
        # Form is checked using Djangos form view
        if self.request.method == 'POST':
            if form.is_valid():
                form.instance.poster = self.request.user
                form.save()
                return redirect(self.success_url)
        else:
            form = ReviewNewForm()
        return super().form_valid(form)

# The view that displays a full list of all the reviews using Django list views
class ReviewsListViewStandard(generic.ListView):
    model = Review
    template_name = 'home/reviews_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_title'] = "List of Reviews"
        return context


# The view that displays a list of reviews filtering only the food reviews
class ReviewsListViewFood(generic.ListView):

    def get_queryset(self):
        queryset = Review.objects.filter(type='Food')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_title'] = "List of Food Reviews"
        return context

    template_name = 'home/reviews_list.html'
    paginate_by = 10


# The view that displays a list of reviews filtering only the activitie reviews
class ReviewsListViewActivities(generic.ListView):

    def get_queryset(self):
        queryset = Review.objects.filter(type='Activities')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_title'] = "List of Activity Reviews"
        return context

    template_name = 'home/reviews_list.html'
    paginate_by = 10


# The view that displays a list of reviews filtering only the accommodation reviews
class ReviewsListViewAccommodation(generic.ListView):

    def get_queryset(self):
        queryset = Review.objects.filter(type='Accommodation')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_title'] = "List of Accommodation Reviews"
        return context

    template_name = 'home/reviews_list.html'
    paginate_by = 10


# The view that displays a list of reviews filtering only the current users reviews
class ReviewsListViewAuthent(generic.ListView):

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Review.objects.filter(poster=self.request.user)
        else:
            queryset = Review.objects.none()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user.username
        context['review_title'] = "Reviews by "+user.capitalize()
        return context

    template_name = 'home/reviews_list.html'
    paginate_by = 10


# The view that displays a single review in full
class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'home/review_details.html'
