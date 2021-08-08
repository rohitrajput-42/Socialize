from django.shortcuts import render, redirect
from .models import Post, Like
from profiles.models import Profile
from .forms import PostModelForm, CommentModelForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View

def post_comment_create_list(request):

    if request.user.is_authenticated:
        qs = Post.objects.all()
        customer = Profile.objects.get(user = request.user)

        # FORMS INITIALIZATION #
        post_form = PostModelForm()
        comment_form = CommentModelForm()
        # FORMS INITIALIZATION #

        profile = Profile.objects.get(user = request.user)

        # POST FORM #
        if 'submit_post_form' in request.POST:
            post_form = PostModelForm(request.POST, request.FILES)
            if post_form.is_valid():
                instance = post_form.save(commit = False)
                instance.author = profile
                instance.save()
                post_form = PostModelForm()
        # POST FORM #

        # COMMENT FORM #
        if 'submit_comment_form' in request.POST:
            comment_form = CommentModelForm(request.POST)
            if comment_form.is_valid():
                instance = comment_form.save(commit = False)
                instance.user = profile
                instance.post = Post.objects.get(id = request.POST.get('post_id'))
                instance.save()
                comment_form = CommentModelForm()
        # COMMENT FORM #

        data = {
            'qs': qs,
            'customer': customer,
            'post_form': post_form,
            'comment_form': comment_form,
        }

        return render(request, 'post.html', data)
    else:
        return render(request, 'post.html')

def like_unlike_post(request):

    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id = post_id)
        profile = Profile.objects.get(user = user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user = profile, post_id = post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

            post_obj.save()
            like.save()

    return redirect('home')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)

        if not obj.author.user == self.request.user:
            messages.warning(self.request, "You need yo be the author of this post in order to delete this post!!!...")
        return obj

class PostUpdateview(UpdateView):
    
    form_class = PostModelForm
    model = Post
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        profile = Profile.objects.get(user = self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "You need yo be the author of this post in order to update this post!!!...")
            return super().form_invalid(form)

