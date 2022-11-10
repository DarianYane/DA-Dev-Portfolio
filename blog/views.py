from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "blog/bloghome.html"
    ordering = ['-updated']

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/postdetail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        sum_likes = stuff.sum_likes()

        liked = False
        
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["sum_likes"] = sum_likes
        context["liked"] = liked
        return context

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/addnewentry.html"

class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "blog/editentry.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/deleteentry.html"
    success_url = reverse_lazy("BlogListView")

class CreateCategoryView(CreateView):
    model = Category
    template_name = "blog/addnewcategory.html"
    fields = '__all__'

def CategoryView(request, continents):
    category_posts = Post.objects.filter(category=continents)
    return render(request, 'blog/categories.html', {'continents': continents.title(), 'category_posts': category_posts})

def LikePost(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:    
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('PostDetailView', args=[str(pk)]))

def search(request):
    print(1)
    print(request.GET)
    if request.GET['title_search']:
        queryset = request.GET['title_search']
        print(queryset)    
        posts = Post.objects.filter(title__icontains=queryset).all()
        print(posts)
        
        if posts!=[]:
            print(2)
            return render(request, "blog/search_result.html", {'posts': posts, 'search': queryset})

    else:
        queryset = '(No search performed)'
        print(queryset)
        return render(request, 'blog/search_result.html', {'search': queryset})