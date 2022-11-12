from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

for choice in choices:
    choice_list.append(choice)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'category', 'story', 'image', 'author')
        labels = {
            'category': ('Select the continent where you traveled'),
            'story': ('Share your experience'),
            'image': ('Upload the best image of your trip'),
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert a title for your post'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert a subtitle for your post'}),
            'story': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell me about your fantastic experience!'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}), #'type': 'hidden'
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
        }



class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'category', 'story', 'image')
        labels = {
            'category': ('Select the continent where you traveled'),
            'story': ('Share your experience'),
            'image': ('Upload the best image of your trip'),
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert a title for your post'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert a subtitle for your post'}),
            'story': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell me about your fantastic experience!'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
        }