from django.forms import ModelForm
from posts.models import NewPost


class NewPostForm(ModelForm):
    class Meta:
        model = NewPost
        fields = '__all__'


class FilterPostForm(ModelForm):
    class Meta:
        model = NewPost
        fields = ['category']
