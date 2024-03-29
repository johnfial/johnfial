# THIS FILE IS IN (OR WAS COPIED FROM) HERE:
# DJANGO LAB 5, BLOG https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/labs/lab05-blog.md
# PROJECT NAME: blog_project
# APP NAMES: blog_app, users_app

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # auth stuff
# help for authentication at:
# https://github.com/PdxCodeGuild/class_orca/blob/main/3%20Django/docs/05%20-%20User%20Management.md

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    # login_url = 'login'    
    # detailview is using int:pk ....

# it's important that the Mixin goes before CreateView!

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'new_post.html'

    fields = ['title', 'caption', 'photo' ]

    def form_valid(self, form):
        form.instance.author = self.request.user

        return super().form_valid(form)
        # CreateView has a form_valid() function...
        # super means ... before you do what you were going to do anyway... let me add something

class BlogEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):    
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'caption' ]

    # UserPassesTestMixin and MUST PUT IN DEF TEST_FUNC, returns a Boolean
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author
        # many ways to write this, see DeleteView


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    
    # don't do this right now, wait to 'figure it out' IF it's necessary
    # jiist = if in a class, use reverse_lazy, if in a function, use reverse 
    success_url = reverse_lazy('blog_app:home')
    
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author
        # many ways to write this, see EditView


