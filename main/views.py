from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from django.utils import timezone



# Create your views here.

def create(request) :

    if request.user.is_authenticated:
        new_post = Post()
        new_post.title = request.POST['title']
        
        #t수정#
        new_post.writer = request.user
        new_post.pub_date = timezone.now()
        new_post.body = request.POST['body']
        new_post.fanname = request.POST['fanname']
        # new_post.hashtag = request.POST['hashtag']
        new_post.image = request.FILES.get('image')

        new_post.save()

        return redirect('main:detail', new_post.id)
    else :
        return redirect('accounts:login')


def new(request):
    return render(request, 'main/new.html')

def mainpage(request):
    posts = Post.objects.all()
    return render(request, 'main/mainpage.html', {'posts':posts})

def secondpage(request):
    return render(request, 'main/secondpage.html')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    if request.method =='GET':
        comments=Comment.objects.filter(post=post)
        return render(request, 'main/detail.html',{
            'post':post,
            'comments':comments,
        })
        
    elif request.method =="POST":
        new_comment = Comment()
        new_comment.post=post
        new_comment.writer=request.user
        new_comment.content=request.POST['content']
        new_comment.pub_date=timezone.now()
        new_comment.save()
        return redirect('main:detail', id)

def edit(request, id):
    edit_post=Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    if request.user.is_authenticated:

        update_post=Post.objects.get(id=id)
        if request.user==update_post.writer:
            update_post.title = request.POST['title']
            update_post.writer = request.user
            update_post.pub_date = timezone.now() 
            update_post.body = request.POST['body'] 

            update_post.save() 

            return redirect ('main:detail', update_post.id)
    return redirect('accounts:login')

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:mainpage')


def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('main:detail', comment.post.id)

def likes(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('main:detail',post.id)