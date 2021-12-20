from django.shortcuts import render, redirect
from posts.forms import NewPostForm, FilterPostForm
from posts.models import NewPost


def new_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewPostForm()
    return render(request, 'new.html', {'form': form})


def view_post(request):
    form = FilterPostForm()
    data = NewPost.objects.all()
    return render(request, 'view.html', {'data': data, 'form': form})


def search(request):
    if request.method == "POST":
        form = FilterPostForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['category'] == 'View-All':
                return redirect('view_post')

            else:
                data = NewPost.objects.filter(category=form.cleaned_data['category'])

    return render(request, 'view.html', {'data': data, 'form': form})


def view_post_details(request,id):
    data = NewPost.objects.get(id=id)
    return render(request, 'post.html', {'data': data})
