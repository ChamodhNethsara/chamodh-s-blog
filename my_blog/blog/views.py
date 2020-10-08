from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,Comment
from django.utils import timezone


# Create your views here.

def welcome(request):
    new_posts = Post.objects.all()
    new_posts = new_posts[:10]
    return render(request,'blog/welcome.html',{"new_posts":new_posts})

def new(request):
    
    return render(request,'blog/add_new_post.html')

def new_post(request):
    title= request.POST.get('title1',"Hello")
    body = request.POST.get('body',"Hello")
    date_published = timezone.now()
    post = Post(title=title,body=body,date_published=date_published)
    post.save()

    return HttpResponseRedirect(reverse('blog:welcome') )  
    
def delete(request,post_id):
    entry_to_delete = Post.objects.get(pk=post_id)
    entry_to_delete.delete()

    return HttpResponseRedirect(reverse('blog:welcome') )  

def view_post(request,post_id):
    comments_for_the_post =[]
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.all()
    for comment in comments:
        if comment.post.id == post_id:
            
            comments_for_the_post.append(comment)
    

    return render(request,'blog/view_post.html',{'post':post,'comments':comments_for_the_post})

def add_comment(request,post_id):
    post=Post.objects.get(pk=post_id)
    comments_for_the_post =[]
    comment = Comment(date_published=timezone.now(),post=Post.objects.get(pk=post_id),comment=request.POST['comment'])
    comment.save()
    comments = Comment.objects.all()
    for comment in comments:
        if comment.post.id == post_id:
            
            comments_for_the_post.append(comment)
    return render(request,'blog/view_post.html',{'post':post,'comments':comments_for_the_post})

def all_posts(request):
    posts = Post.objects.all()
    return render(request,'blog/all_posts.html',{'posts':posts})