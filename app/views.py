from django.shortcuts import render, redirect
from .forms import registration_form,student_form
from .models import *
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import redirect_authenticated_user
from django.contrib.auth.mixins import LoginRequiredMixin

def home_page(request):
    stud = Student.objects.all()
    context = {'stud':stud}
    return render(request, 'app/home.html', context)


class student_page(ListView):
    model = Student
    template_name = 'app/student.html'
    context_object_name = "students"
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['total_dept'] = Department.objects.count()
        context['total_graduates'] = Student.objects.filter(current_level__gt=models.F('level_duration')).count()
        return context

class profile_page(LoginRequiredMixin, DetailView):
    login_url = 'login_page'
    model = Student
    template_name = 'app/profile.html'
    context_object_name = "students"
        
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['total_dept'] = Department.objects.count()
        context['total_graduates'] = Student.objects.filter(current_level__gt=models.F('level_duration')).count()
        return context

    def get_object(self):
        return Student.objects.get (user=self.request.user)

@redirect_authenticated_user
def register_page(request):
    form = registration_form() 

    if request.method == 'POST':   
        form = registration_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Successfully Created')
            return redirect('student_page')  # replace with your URL name

    return render(request, 'auth/register.html', {'form': form})


@redirect_authenticated_user
def student_login(request):
    if request.method == 'POST':
        matric = request.POST.get('matric_num')
        password = request.POST.get('password')
        print("Matric entered:", matric)
        print("Password entered:", password)
        try:
            student = Student.objects.get(matric_num=matric)
            user = student.user   # get the related CustomUser
            print("Student found:", student)
            print("User email:", student.user.email)
            user = authenticate(request, email=user.email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_page')
            else:
                messages.error(request, 'Invalid matric number or password.')

        except Student.DoesNotExist:
            messages.error(request, 'User with this matric number does not exist.')
    
    return render(request, 'auth/login.html')

def logout_page(request):
    logout(request)
    messages.info(request, 'Account Successfully Logout')
    return redirect('login_page')


def student_create_account(request):
    # Check if the logged-in user already has a Student account
    if request.user.is_authenticated and hasattr(request.user, 'student'):
        messages.info(request, 'You already have an Account')
        return redirect('profile_page')
    form = student_form()
    if request.method == 'POST':
        form = student_form(request.POST, request.FILES)  # <-- bind data
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if CustomUser exists
            try:
                user = custom_user.objects.get(email=email)
            except custom_user.DoesNotExist:
                messages.error(request, 'No account with this email exists. Kindly register first.')
                return render(request, 'app/create_user.html', {'form': form})

            # Prevent duplicate Student account
            if Student.objects.filter(user=user).exists():
                messages.error(request, "A student account for this email already exists.")
                return render(request, 'app/create_user.html', {'form': form})

            # Create Student linked to CustomUser
            student = form.save(commit=False)
            student.user = user
            student.save()
            messages.success(request, "Student account successfully created! Your matric number will be sent to your email.")
            return redirect('login_page')
        else:
            messages.error(request, "Please correct the errors below.")  # Show form errors

    return render(request, 'app/create_user.html', {'form': form})