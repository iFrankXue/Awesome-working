from django import forms
from .models import Post, Comment

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['url', 'body', 'tags']
        labels = {
            'body': 'Caption',
            'tags': 'Category'
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Add a caption ...', 
                'class': 'font1 text-4xl'}),
            'url': forms.TextInput(attrs={
                'id': 'url-input',
                'placeholder': 'Add url ...'
            }),
            'tags': forms.CheckboxSelectMultiple(),
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body': '',
            'tags': 'Category',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'class': 'font1 text-4xl'
            }),
            'tags': forms.CheckboxSelectMultiple(),
        }
        

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs = {
                'placeholder': 'Add comment ...'
            })
        }
        labels = {
            'body': ''
        }
        

# # forms.py
# from django import forms
# from .models import Comment

# class CommentAdminForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Filter parent_comment queryset if a parent_post is available and defined
#         if self.instance.pk and hasattr(self.instance, 'parent_post') and self.instance.parent_post:
#             self.fields['parent_comment'].queryset = Comment.objects.filter(parent_post=self.instance.parent_post)
#         else:
#             self.fields['parent_comment'].queryset = Comment.objects.none()  # Empty queryset if no parent_post is selected