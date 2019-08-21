import logging

from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import generic
from .models import Review
from .forms import SignUpForm, ReviewNewForm

log = logging.getLogger(__name__)

def home(request):
    meta = {
        'title': 'Home',
        'description': 'Parkafreebia II home page where you can see a quick rundown of the page and its features'
    }
    return render(request, 'home/home.html', meta)


def history(request):
    meta = {
        'title': 'History',
        'description': 'Parkafreebia II a short history of the app and the prosess that created it'
    }
    return render(request, 'home/aboutHistory.html', meta)


def contact(request):
    meta = {
        'title': 'Contact Us',
        'description': 'Parkafreebia II contact page, the form used to submit reviews and bug reports'
    }
    return render(request, 'home/contactUs.html', meta)


def contribute(request):
    meta = {
        'title': 'Contribute',
        'description': 'Parkafreebia II contributers page where you go to get the app development kit'
    }
    return render(request, 'home/contribute.html', meta)

def privacyPolicy(request):
    meta = {
        'title': 'Privacy Policy',
        'description': 'Parkafreebia II privacy policy page updated 21st august 2018'
    }
    return render(request, 'home/privacyPolicy.html', meta)


def termsOfService(request):
    meta = {
        'title': 'Terms of Service',
        'description': 'Parkafreebia II terms of service page updated august 21st 2018'
    }
    return render(request, 'home/termsOfService.html', meta)


def theMaking(request):
    meta = {
        'title': 'The Making',
        'description': 'Parkafreebia II information on the making of the app and how it was coded'
    }
    return render(request, 'home/theMaking.html', meta)

def logout(request):
    log.warning(request.user.username + ' Logged out')
    django_logout(request)
    return render(request, 'registration/logged_out.html')

def reset_request(request):
    log.warning('Password change request made')
    return render(request, 'registration/password_reset_form.html')

def signup(request):
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
    return render(request, 'registration/signup.html', {'form': form})

class NewReviewView(generic.FormView):
    template_name = 'home/new_review.html'
    form_class = ReviewNewForm
    success_url = '/home'

    def form_valid(self, form):

        if self.request.method == 'POST':
            if form.is_valid():
                form.instance.poster = self.request.user
                form.save()
                return redirect(self.success_url)
        else:
            form = ReviewNewForm()
        return super().form_valid(form)


class ReviewsListViewStandard(generic.ListView):
    model = Review
    template_name = 'home/reviews_list_standard.html'
    paginate_by = 10


class ReviewsListViewAuthent(generic.ListView):
    model = Review
    template_name = 'home/reviews_list_authenticated.html'
    paginate_by = 10


class ReviewDetailView(generic.DetailView):
    model = Review
    template_name = 'home/review_details.html'
