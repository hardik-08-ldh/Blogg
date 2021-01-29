from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from blog import models,forms
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
# Create your views here.
# def home(request):
#     return render(request,'home.html',{})
class Home(ListView):
    model=models.Post
    context_object_name='post'
    template_name='home.html'
    ordering=['-created_at','-id']

    def get_context_data(self,*args,**kwargs):
        cat_menu=models.Category.objects.all()
        new_context=super(Home,self).get_context_data(*args,**kwargs)
        new_context['cat_menu']=cat_menu
        return new_context

def CategoryView(request,cats):
    cats=cats.replace('-',' ')
    cat_posts=models.Post.objects.filter(category=cats.title())
    return render(request,'categoryarticle.html',{'cat_posts':cat_posts,'cats':cats.title()})

def CategoryDetail(request):
    cat_list=models.Category.objects.all().order_by('name')
    context={
        'cat_list':cat_list
    }
    return render(request,'category_detail.html',context)

class ArticleView(DetailView):
    model=models.Post
    context_object_name='article'
    template_name='article_detail.html'

    def get_context_data(self,*args,**kwargs):
        cat_menu=models.Category.objects.all()
        new_context=super(ArticleView,self).get_context_data(*args,**kwargs)
        like_object=get_object_or_404(models.Post,id=self.kwargs['pk'])
        total_likes=like_object.total_likes()
        liked=False

        if like_object.like.filter(id=self.request.user.id).exists():
            liked=True
        new_context['total_likes']=total_likes
        new_context['cat_menu']=cat_menu
        new_context['liked']=liked
        return new_context

class AddPostView(CreateView):
    model=models.Post
    form_class=forms.PostForm
    context_object_name='post'
    template_name='add_post.html'
    # login_url='not_authenticated'
    # fields='__all__'
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super(AddPostView, self).form_valid(form)

    def get_context_data(self,*args,**kwargs):
        cat_menu=models.Category.objects.all()
        new_context=super(AddPostView,self).get_context_data(*args,**kwargs)
        new_context['cat_menu']=cat_menu
        return new_context

class UpdatePostView(UpdateView):
    model=models.Post
    form_class=forms.EditForm
    context_object_name='post'
    template_name='update_post.html'
    # login_url='not_authenticated'
    # fields={'title','body'}
    def get_context_data(self,*args,**kwargs):
        cat_menu=models.Category.objects.all()
        new_context=super(UpdatePostView,self).get_context_data(*args,**kwargs)
        new_context['cat_menu']=cat_menu
        return new_context

class DeletePostView(DeleteView):
    model=models.Post
    context_object_name='post'
    template_name='delete_post.html'
    # login_url='not_authenticated'
    success_url=reverse_lazy('home')
    def get_context_data(self,*args,**kwargs):
        cat_menu=models.Category.objects.all()
        new_context=super(DeletePostView,self).get_context_data(*args,**kwargs)
        new_context['cat_menu']=cat_menu
        return new_context

# class NotAllowed(TemplateView):
#     template_name = "not_authenticated.html"
def LikeView(request,pk):
    post=models.Post.objects.get(id=pk)
    liked=False
    if post.like.filter(id=request.user.id).exists():
        liked=False
        post.like.remove(request.user)
    else:
        liked=True
        post.like.add(request.user)
    # print(request.POST.get('postid'))
    # post=get_object_or_404(models.Post,id=request,POST.get(pk))
    # like_object=get_object_or_404(models.Post,id=self.kwargs['pk'])
    return HttpResponseRedirect(reverse('article',args=[str(pk)]))


class AddCommentView(CreateView):
    model=models.Comment
    form_class=forms.CommentForm
    # fields='__all__'
    template_name='add_comment.html'
    success_url=reverse_lazy('home')

    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
