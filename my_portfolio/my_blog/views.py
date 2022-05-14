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
    model = Post
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 5
    template_name = 'my_blog/posts/post_list.html'


class TaggedListView(DetailView):
    # queryset = Tag.objects.filter(tags__name__in=['tag'])
    template_name = "my_blog/posts/tag_detail.html"
    context_object_name = 'tags'

    def get_queryset(self):

        print(Post.objects.filter(tags__slug=self.kwargs.get('slug')))
        return Tag.objects.filter(slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super(TaggedListView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        print(context)
        return context


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
