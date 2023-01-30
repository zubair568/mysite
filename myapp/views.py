from django.contrib import auth, messages
from django.db.models import Model
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, Post
from .forms import Form, PostForm


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return render(request,'login.html')
    else:
        post = Post.objects.all()
        return render(request,'index.html', {'post': post})

def registration(request):
    if request.method == 'POST':
        user = Form(request.POST)
        f_name = request.POST.get("f_name")
        l_name = request.POST.get('l_name')
        phone_no = request.POST.get("phone_no")
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if user.is_valid():
                user = Member.objects.create(username=username,
                                                 email=email, password=password, f_name=f_name, l_name=l_name,
                                                 phone_no=phone_no)

                user.save()
                messages.info(request, 'Congratulation! You account has been register.')
                return redirect('login_user')

    else:
        return render(request, 'registration.html', {})

def login_user(request):
     if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('index')

            else:
                messages.info(request, 'Invalid Username or Password')
                return redirect('login_user')
     else:
        return render(request, 'login.html')

def logout(request):
    return render(request, 'login.html')

def post_detail(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form = PostForm()
            messages.success(request, "Successfully created")
    return render(request, 'form.html', {'form': form})

def edit(request, id):
    context = {}
    obj = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("index")

    context["form"] = form

    return render(request, "edit.html", context)

def delete(request, pk):
        Post.objects.filter(id=pk).delete()
        return redirect('index')