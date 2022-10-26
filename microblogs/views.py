from django.shortcuts import redirect,render
from .forms import LogInForm,SignUpForm



# Create your views heres.
def home(request):
    return render(request,'home.html')


def log_in(request):
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
