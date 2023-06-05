from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect,render, get_object_or_404
from .forms import LogInForm,SignUpForm,PostForm
from django.contrib import messages
from .models import Post, User
from django.http import HttpResponseForbidden
from django.core.exceptions import ObjectDoesNotExist
from .helpers import login_prohibited
from django.db.models import Count


# Create your views heres.



@login_prohibited
def home(request):
    return render(request,'home.html')

@login_prohibited
def log_in(request):
    # post request
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            #extract username and pass and see if comb is is_valid
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password) #search for user record and see if password hash is the same, and return user
            if user is not None:
                login(request,user) #how
                redirect_url = request.POST.get('next') or 'feed'
                return redirect(redirect_url)
        #Add error message
        messages.add_message(request, messages.ERROR, "The credentials provided is invalid!")
        
    # get request
    form = LogInForm()
    next = request.GET.get('next') or ''
    return render(request,'log_in.html', {'form' : form, 'next': next}) #view needs to be rendered with form

@login_prohibited
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) #create bound version of form with post data
        if form.is_valid():
            user = form.save()
            login(request,user) #how?
            return redirect('feed')
    else:
        form = SignUpForm()

    return render(request,'sign_up.html', {'form' : form})

def log_out(request):
    logout(request)
    return redirect('home')

#login_required: if user logged in fucntion is applied: otherwise user is redirected
@login_required
def feed(request):
    form = PostForm
    current_user = request.user
    posts = Post.objects.all()
    return render(request, 'feed.html', {'form': form, 'posts':posts , 'request_user': request.user})


def new_post(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            current_user = request.user
            form = PostForm(request.POST)
            if form.is_valid():
                text = form.cleaned_data.get('text')
                post = Post.objects.create(author=current_user, text=text)
                return redirect('feed')
            else:
                return render(request, 'feed.html', {'form': form})
        else:
            return redirect('log_in')
    else:
        return HttpResponseForbidden()

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def like_post(request, pk):
    try:
        post = Post.objects.get(id=pk)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)  
        else:
            post.likes.add(request.user)
    except ObjectDoesNotExist:
        return redirect('feed')
    else:
       return redirect(request.META.get('HTTP_REFERER', 'feed'))
      

@login_required
def follows_user(request, pk):
    try:
        user = User.objects.get(id=pk)
        if user.follows.filter(id=request.user.id).exists():
            user.follows.remove(request.user)  
        else:
            post.follows.add(request.user)      
    except ObjectDoesNotExist:
        return redirect('feed')
    else:
        return redirect('feed')



@login_required
def show_user_feed(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        posts = Post.objects.filter(author=user)
    except ObjectDoesNotExist:
        return redirect('feed')
    else:
        return render(request, 'show_user.html', {'user': user , 'posts' : posts, 'request_user': request.user})


@login_required
def show_user(request, user_id):

    try:
        user = get_object_or_404(
            User.objects.annotate(total_likes=Count('post__likes')), pk=user_id
        )
        posts = Post.objects.filter(author=user)
    except ObjectDoesNotExist:
        return redirect('user_list')
    else:
        return render(request, 'show_user.html', {'user': user , 'posts' : posts, 'request_user': request.user})
        
