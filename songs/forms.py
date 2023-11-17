from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'artist',
            'album',
            'year',
            'cover',
            'lyrics',
        ]
        labels = {
            'title': 'Título',
            'artist': 'Artista',
            'album': 'Álbum',
            'year': 'Ano',
            'cover': 'Capa',
            'lyrics': 'Letra',
        }
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Comentário',
        }