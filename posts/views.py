from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from .models import Post

# Create your views here.
def index(request):
    #to check if method is post
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        #check if the form is valid or not 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
            # return HttpResponse("Error")
    posts=Post.objects.all().order_by('-created_at')[:20]
    return render(request, 'posts.html',{'posts': posts})

def delete(request, post_id):
    #To find which post to be deleted 
    post =Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def LikeView(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes + 1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'GET':
        return render(request, 'edit.html', {'posts' : post})
    if request.method == 'POST':
        editposts=Post.objects.get(id=post_id)
        form= PostForm(request.POST,request.FILES,instance=editposts)
        if form.is_valid():
            #Yes, save
            form.save()
            #Redirect to Home
            return HttpResponseRedirect('/')
        else:
            # No, Show Error Error
            return HttpResponseRedirect(form.errors.as_json())
    
def edit(request,post_id):
    post=Post.objects.get(id=post_id)
    if request.method=="GET":
        return render(request,"edit.html",{"post":post})
    if request.method=="POST":
        editposts=Post.objects.get(id=post_id)
        form=PostForm(request.POST,request.FILES,instance=editposts)
        if form.is_valid():

                #yes Save
            form.save()
                #redirect to home
            return HttpResponseRedirect('/') 
        else:
            return HttpResponse("not Valid")
