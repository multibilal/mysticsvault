from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	"""docstring for CommentForm"""
	class Meta:
		model = Comment
		fields = ('user','email','body')
		
		