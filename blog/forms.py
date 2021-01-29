from django import forms
from blog import models

# CHOICES=[('Coding','Coding'),('News','News'),('Sports','Sports')]
# it is one way/|\ other way is \|/
CHOICES=models.Category.objects.all().values_list('name','name').order_by('name')
# CHOICES_LIST=[]
# for item in CHOICES:
#     CHOICES_LIST.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=('title','author','category','body','snippet','header_image')
        widgets={
            # form class in bootstrap given to input fields attrs contains all input attributes
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','type':'hidden','id': 'Author'}),
            # 'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=CHOICES,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model=models.Post
        fields=('title','body','snippet')
        widgets={
            # form class in bootstrap given to input fields attrs contains all input attributes
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter title'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'snippet':forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=('name_of_user','body')
        widgets={
            'name_of_user':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
       }