from django import forms
from .models import Review

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ReviewForm(forms.ModelForm):

	class Meta:
		model = Review
		fields = ('rating', 'comment')
