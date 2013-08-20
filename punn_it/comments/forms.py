from django.utils.translation import ugettext as _
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': _('Submit a comment...'),
                                             'id': 'comment-box', 
                                             'rows': '1',
                                             'class': 'form-control',}),
        }


