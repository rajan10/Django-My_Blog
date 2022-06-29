from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.core.mail import send_mail


def index(request):
    context={}
    object_list=Post.objects.all()
    # show 5 objects  in one page
    pagin=Paginator(object_list,10)
    # GET variables and they usually appear in the address bar, e.g http: // 127.0.0.1: 8000 /?page = 2
    # .get() is a python method that is normally used to return the value of items with a specific key from a dictionary.If nothing is found None is returned.
    page_number=request.GET.get('page')
    page_obj=pagin.get_page(page_number)
    context['page_obj']=page_obj
    # only sending the context of object that is
    context['object_list']=page_obj.object_list
    return render(request, template_name="index.html",  context=context)

# def header(request):
#     context={}
#     posts=Post.objects.all()
#     context['posts']=posts
#     return render(request, template_name="header.html", context=context)

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


# create comment is inside detail_post
@login_required(login_url='/login')
def detail_post(request, id):
    if request.method=="GET":
        post=get_object_or_404(Post, pk=id)
        context={}
        context['post']=post
        context['form']=CommentForm()
        return render(request, template_name='detail.html',context=context)

    if request.method=="POST":
        commentor=request.user
        post = get_object_or_404(Post, pk=id)
        form=CommentForm(request.POST)
        if form.is_valid():
            content=form.cleaned_data['content']
            comment=Comment(commentor=commentor, post=post, content=content)
            comment.save()
            # redirect to same page
            return redirect(request.path_info)

def update_comment(request, id):
    comment=get_object_or_404(Comment, pk=id)
    if request.method=="GET":
            if request.user==comment.commentor:
                context={}
                data = {'content':comment.content}
                form=CommentForm(data)
                context['form']=form
                context['post']=comment.post
                return render(request, template_name="detail.html",context=context)
            else:
                return HttpResponse("You are not allowed to edit/update due to create violiation Rule")
    if request.method=="POST":
        form=CommentForm(request.POST)
        if form.is_valid():
            content=form.cleaned_data['content']
            comment.content=content
            comment.save(update_fields=['content'])
            return redirect(request.path_info)
# this id is for comment
def delete_comment(request, id):
    comment=get_object_or_404(Comment, pk=id)
    print(comment)
    # comment=Post.posts.get(pk=id)
    # if request.method=="POST":
    # print(comment)
    if request.user==comment.commentor:
        comment.delete()
        # below pk is for post unique id
        pk=comment.post.pk
        print(comment.post.title)
        print(comment.post.content)
        print(comment.post.created_date)
        return redirect(f'/detail_post/{ pk }')
    else:
        return HttpResponse("You are not allowed to  delete this comment due to Create Violiation Rule")


@login_required(login_url='/login')
def delete_post(request, id):
    post=Post.objects.filter(pk=id)
    post.delete()
    return redirect('/')

def sending_mail(request):
    subject='About vacation-this is subject.'
    message='Here is the message.'
    sender_email='rajangauchan10@gmail.com'
    receiver_email=['lxmnmrzn@gmail.com']
    fail_silently=False

    send_mail(subject,message, sender_email,receiver_email,fail_silently)
    return HttpResponse("Message is sent!")