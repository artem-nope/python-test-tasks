from django.forms import ModelForm
from .models import *


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ['username', 'text']