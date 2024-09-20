from django.shortcuts import render
from django.views.generic import TemplateView
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class IndexView(TemplateView) :
    def get(self, request) :
        return render(request, 'main/index.html')


class HomeView(LoginRequiredMixin ,TemplateView) :
    def get(self, request) :
        data = SocialAccount.objects.get(user=request.user).extra_data
        context = {
            'data' : data
        }
        return render(request, 'main/home.html', context)