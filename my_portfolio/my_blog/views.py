from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def post_list(request, tag_slug=None):
    Tags = Tag.objects.all()
    posts = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'my_blog/posts/post_list.html',
                  {'posts': posts,
                   'tag': tag,
                   'Tags': Tags,
                   'page': page})
    # take all object's parameter

    # return site with |post| data from data base


# def tag_list(request, tag_slug=None):
#     posts= Post.objects.all()
#     tag = None
#     if tag_slug:
#         tag = get_object_or_404(Tag, slug=tag_slug)
#         posts = posts.filter(tags__in=[tag])
#
#     return render(request,
#                   'my_blog/posts/post_tag.html',
#                   {'posts': posts,
#                    'tag': tag})
class PostListView(ListView):
    model = post_list
    queryset = Post.published.all()
    context_object_name = 'posts'

    paginate_by = 5
    template_name = 'my_blog/posts/post_list.html'


class TaggedListView(DetailView):
    model = post_list
    queryset = Post.objects.all()
    paginate_by = 3
    template_name = "my_blog/posts/post_list.html"

    def get_queryset(self, tag):
        return Post.objects.filter(tags__name__in=[tag])


def post_detail(request, year, month, day, post):
    details = get_object_or_404(Post, slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)

    # object that retrieves information from a database based on a post model

    comments = details.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = details
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'my_blog/posts/post_detail.html',
                  {'details': details,
                   'comments': comments,
                   'comment_form': comment_form})
    # return site with detail data |post|
