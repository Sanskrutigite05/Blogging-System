from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Blog,Category

# Create your views here.


def posts_by_category(request,category_id):
    #fetch the posts that belong to the category with the id category_id
    
    posts=Blog.objects.filter(status='Published',category_id = category_id)
    # try:                                                           #this whole try and catch shows u correct category page and if the categor page dosen't exist it redirect u to home
    #     category=Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    category=get_object_or_404(Category,id=category_id)   #this basically shows page not found to user
    
    context={
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)
    