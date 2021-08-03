from django.utils.translation import activate
from .forms import Comment_form
from django.core import paginator
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.core.paginator import Paginator

# Create your views here.
from .models import Comment, Post
def post_list(request):
    post = Post.objects.filter(status = 'published')
    paginator = Paginator(post,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'page_obj':page_obj
    }
    return render(request, 'post_list.html', context )

def detail_list(request, year, month, day, slug):
    # try:
    #     post = Post.objects.get(created_date__year=year,
    #     created_date__month=month,
    #     created_date__day=day,
    #     slug = slug,
    #     status = True)
    # except Post.DoesNotExist:
    #     raise Http404('این پست وجود ندارد')

    post = get_object_or_404(Post,created_date__year=year,
        created_date__month=month,
        created_date__day=day,
        slug = slug,
        status = 'published')
    comment_form = Comment_form(request.POST or None)
    if comment_form.is_valid():
        name = comment_form.cleaned_data.get('name')
        email = comment_form.cleaned_data.get('email')
        message = comment_form.cleaned_data.get('comment')
        Comment.objects.create(post = post, name = name, email = email, comment = message, activate = False)
        comment_form = Comment()


    context = {
        'post':post,
        'comment_form':comment_form,
    }

    return render(request, 'post_detail.html', context)

def contact_us(request):
    return render(request, 'contact_us.html')
    
