from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import FormView,UpdateView
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.contrib.auth.models import User
# from .models import 

# Create your views here.


def edit_profile(request):
    
        if request.method=='POST':
            profile_form = RegisterForm(request.POST , instance = request.user )
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Profile update Successfully Completed')

            return redirect('profile')
        
        else:
         profile_form = RegisterForm( instance = request.user)  
        return render(request, 'edit_profile.html' , {'form' : profile_form } )



def profile(request):
    return render(request,'profile.html' )

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('log_in')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request , 'Registerd Successfully Finished...')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request , 'Invalid information ,Try again')
        return super().form_invalid(form)
        

class Log_inView(LoginView):
    template_name = 'log_in.html'
    # form_class = RegisterForm
    
    def get_success_url(self) :
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request , 'Log In  Successfully Finished...')
        return super().form_valid(form)
    
    
    def form_invalid(self, form):        
       messages.info(self.request , 'Invalid Information...')
       return super().form_invalid(form)
        
    
    


class Log_out(LogoutView):
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def dispatch(self,  request ,  *args , **kwargs) :
        messages.success(self.request , "Log Out Successfull")
        return super().dispatch(self.request, *args, **kwargs)