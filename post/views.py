from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

def index(request):
    context={}
    # if request.user:
    #     # print("logged in user")
    #     context['user']=request.user
    #     return render(request, template_name='index.html', context=context)
    # else:
    #     print("no  user ")
    #     return render(request, template_name='index.html',context=context)
    posts=Post.objects.all()
    context['posts']=posts
    return render(request, template_name="index.html", context=context)




@login_required(login_url='/login')
def create_post(request):
    if request.method=="GET":
        context={}
        form=PostForm()
        context['form']=form
        return render(request,template_name="create_post.html", context=context)
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            author = request.user
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            content = form.cleaned_data['content']
            post=Post(author=author,title=title,image=image,content=content)
            post.save()
            return redirect('index')
        else:
            print("form is invalid")
            return redirect('index')

@login_required(login_url='/login')
def update_post(request, id):
    post=get_object_or_404(Post, pk=id)
    if request.method=="GET":
        data={'title':post.title,'image':post.image,'content':post.content}
        form=PostForm(data)
        context={}
        context['form']=form
        return render(request, template_name='update_post.html', context=context)
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            # post.author=form.cleaned_data['author']
            post.title=form.cleaned_data['title']
            post.image=form.cleaned_data['image']
            post.content=form.cleaned_data['content']
            post.save(update_fields=['title','image','content'])
            return redirect('/')
        else:
            print("form is invalid")
            return redirect('/')

@login_required(login_url='/login')
def delete_post(request, id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect('/')