from django.shortcuts import redirect,render
from .forms import SignUpForm



# Create your views heres.
def home(request):
    return render(request,'home.html')


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

# Create your views here.
def log_in(request):
    return render(request,'log_in.html')
