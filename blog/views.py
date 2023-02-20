from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.

#List of all the posts ordered from newest to oldest
class BlogListView(ListView):
    model = Post
    template_name = "blog/bloghome.html"
    ordering = ['-updated']

#View of each post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/postdetail.html"

    #View the likes of the post
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

#Create a blog entry
class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/addnewentry.html"

#Update a blog entry
class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = "blog/editentry.html"

#Delete a blog entry
class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/deleteentry.html"
    success_url = reverse_lazy("BlogListView")

#Create a category
class CreateCategoryView(CreateView):
    model = Category
    template_name = "blog/addnewcategory.html"
    fields = '__all__'

#View categories
def CategoryView(request, continents):
    category_posts = Post.objects.filter(category=continents)
    return render(request, 'blog/categories.html', {'continents': continents.title(), 'category_posts': category_posts})

#Like/unlike a post
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

#Search by post title
def search(request):
    print(request.GET)
    if request.GET['title_search']:
        queryset = request.GET['title_search']
        print(queryset)    
        posts = Post.objects.filter(title__icontains=queryset).all()
        print(posts)
        
        if posts!=[]:
            return render(request, "blog/search_result.html", {'posts': posts, 'search': queryset})

    else:
        queryset = '(No search performed)'
        print(queryset)
        return render(request, 'blog/search_result.html', {'search': queryset})