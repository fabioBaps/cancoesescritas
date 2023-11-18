from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.views import generic
    
    
    
# def ListView(request):
#     post_list = Post.objects.all()
#     return render(request, 'songs/list.html', {'post_list': post_list})

# def DetailView(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     return render(request, 'songs/detail.html', {'post': post})

# def CreateView(request):
#     if request.method == 'POST':
#         post_title = request.POST['title']
#         post_artist = request.POST['artist']
#         post_album = request.POST['album']
#         post_year = request.POST['year']
#         post_cover = request.POST['cover']
#         post_lyrics = request.POST['lyrics']
#         post = Post(title=post_title,
#                       artist=post_artist,
#                       album=post_album,
#                       year=post_year,
#                       cover=post_cover,
#                       lyrics=post_lyrics)
#         post.save()
#         return HttpResponseRedirect(
#             reverse('songs:detail', args=(post.id, )))
#     else:
#         return render(request, 'songs/create.html', {})
    
# def UpdateView(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)

#     if request.method == "POST":
#         post.title = request.POST['title']
#         post.artist = request.POST['artist']
#         post.album = request.POST['album']
#         post.year = request.POST['year']
#         post.cover = request.POST['cover']
#         post.lyrics = request.POST['lyrics']
#         post.save()
#         return HttpResponseRedirect(
#             reverse('songs:detail', args=(post.id, )))

#     context = {'post': post}
#     return render(request, 'songs/update.html', context)

# def DeleteView(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)

#     if request.method == "POST":
#         post.delete()
#         return HttpResponseRedirect(reverse('songs:list'))

#     context = {'post': post}
#     return render(request, 'songs/delete.html', context)

# class postFormListView(generic.ListView):
#     model = Post
#     template_name = 'songs/list.html'

    
# class postFormDetailView(generic.DetailView):
#     model = Post
#     template_name = 'songs/detail.html'

# class postFormCreateView(generic.CreateView):
#     model = Post
#     template_name = 'songs/create.html'
#     fields = ['title', 'artist', 'album', 'year', 'cover', 'lyrics']
#     def get_success_url(self):
#         return reverse('songs:detail', kwargs={'pk': self.object.pk})

# class postFormUpdateView(generic.UpdateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'songs/update.html'
#     def get_success_url(self):
#         return reverse('songs:detail', kwargs={'pk': self.object.pk})

# class postFormDeleteView(generic.DeleteView):
#     model = Post
#     template_name = 'songs/delete.html'
#     success_url = reverse_lazy('songs:list')
    

class postListView(generic.ListView):
    model = Post
    template_name = 'songs/list.html'
    
class postDetailView(generic.DetailView):
    model = Post
    template_name = 'songs/detail.html'
    
class postCreateView(generic.CreateView):
    model = Post
    template_name = 'songs/create.html'
    fields = ['title', 'artist', 'album', 'year', 'cover', 'lyrics']
    def get_success_url(self):
        return reverse('songs:detail', kwargs={'pk': self.object.pk})
    
class postUpdateView(generic.UpdateView):
    model = Post
    template_name = 'songs/update.html'
    fields = ['title', 'artist', 'album', 'year', 'cover', 'lyrics']
    def get_success_url(self):
        return reverse('songs:detail', kwargs={'pk': self.object.pk})
    
class postDeleteView(generic.DeleteView):
    model = Post
    template_name = 'songs/delete.html'
    def get_success_url(self):
        return reverse('songs:list')
    

def SearchView(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(title__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'songs/search.html', context)

def commentCreateView(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('songs:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'songs/create_comment.html', context)


class categoryListView(generic.ListView):
    model = Category
    template_name = 'songs/categorys.html'
    
class categoryDetailView(generic.DetailView):
    model = Category
    template_name = 'songs/detail_category.html'
    
class categoryCreateView(generic.CreateView):
    model = Category
    template_name = 'songs/create_category.html'
    fields = ['name', 'description', 'author', 'songs']
    success_url = reverse_lazy('songs:categorys')