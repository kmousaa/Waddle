from django.contrib.auth import authenticate,login
from django.shortcuts import redirect,render
from .forms import LogInForm,SignUpForm



# Create your views heres.
def home(request):
    return render(request,'home.html')


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            #extract username and pass and see if comb is is_valid
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #built in django
            if user is not None:
                login(request,user)
                return redirect('feed')

    form = LogInForm()
    return render(request,'log_in.html', {'form' : form}) #view needs to be rendered with form


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) #create bound version of form with post data
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = SignUpForm()

    return render(request,'sign_up.html', {'form' : form})

def feed(request):
    return render(request,'feed.html')
