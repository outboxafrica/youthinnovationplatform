from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, FormView
from blog.models import Post
from . forms import CommentForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all().filter(status="published")
    if len(posts) == 0:
        latest_post = None
    elif len(posts) > 0:
        latest_post = posts[0]
        posts = posts[1:]
    return render(request,
                  'blog/post_list.html',
                  {'posts': posts, 'latest_post': latest_post})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    else:
        form = CommentForm()
    form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post':post, 'commentForm': form})


class PostList(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        posts = Post.objects.all().filter(status="published")
        print "Posts ", len(posts)
        if len(posts) > 0:
            latest_post = posts[0]
            posts = posts[1:]
        else:
            posts = None
            latest_post = None
        context['posts'] = posts
        context['latest_post'] = latest_post
        return context











