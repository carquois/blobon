# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, URLField, ImageField, ModelMultipleChoiceField
from django.utils.translation import ugettext as _

from blogs.models import Blog, Post, Category

class BlogForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Enter your title'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    slug = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog adress'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    class Meta:
        model = Blog 
        fields = ('title', 'slug', )

class SubmitForm(ModelForm):
    title = CharField(label=_('Title :'), widget=forms.TextInput(attrs={'placeholder': _('Enter your title here.'), 'class': 'form-control'}), required=False)
    translated_title = CharField(label=_('Title translated :'), widget=forms.TextInput(attrs={'placeholder': _('Enter your translation here.'), 'class': 'form-control'}), required=False)
    source = URLField(label=_('Source :'), widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Post
        fields = ('title', 'translated_title',)

class SettingsForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog title'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    slug = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog adress'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    password = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog password'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    custom_domain = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your custom domain'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    description = CharField(widget=forms.Textarea(attrs={'placeholder': _('Describe Your Blog'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level"}))    
    class Meta:
        model = Blog 
        fields = ('title', 'slug', 'password', 'custom_domain','description', )



class CategoriesForm(ModelForm):
    name = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your category name here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    description = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Describe your category'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level"}))
    slug = CharField(widget=forms.TextInput(attrs={'placeholder': _('Slug'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    class Meta:
        model = Category
        fields = ('name','description','slug', )


class PostForm(ModelForm):
    title = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Write your title here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    source = URLField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Your source'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    artist = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Write artist name here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write a new post'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    text = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write your text here'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    category = ModelMultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())
    content_0 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content_01 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    content_1 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_2 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_3 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_4 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_5 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_6 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev",
                                                    'autofocus':'on'}))
    content_video = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this video'),
                                                    'type': 'text',
                                                    'rows': '3',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    youtube_url = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Copy a Youtube url here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    pic_1 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_1(this);"}))
    pic_2 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_2(this);"}))
    pic_3 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_3(this);"}))
    pic_4 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_4(this);"}))
    pic_5 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_5(this);"}))
    pic_6 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_6(this);"}))
    pic_7 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_7(this);"}))
    pic_8 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_8(this);"}))
    pic_9 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_9(this);"}))
    pic_10 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_10(this);"}))
    pic_11 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_11(this);"}))
    pic_12 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_12(this);"}))
    pic_13 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_13(this);"}))
    pic_14 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_14(this);"}))
    pic_15 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_15(this);"}))
    pic_16 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_16(this);"}))
    pic_17 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_17(this);"}))
    pic_18 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_18(this);"}))
    pic_19 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_19(this);"}))
    pic_20 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_20(this);"}))
    pic_21 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_21(this);"}))
    pic_22 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_22(this);"}))
    pic_23 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_23(this);"}))
    pic_24 = ImageField(required=False, widget=forms.FileInput(attrs={'onchange':"upload_img_24(this);"}))
    class Meta:
        model = Post
        exclude=('author',) 
        fields = ('title','content','source','status','artist','text','content_0','content_01','content_1','content_2','content_3','content_4','content_5','content_6','content_video', 'pic','pic_0','pic_04','pic_1','pic_2','pic_3','pic_4','pic_5','pic_6','youtube_url','category',
                 'pic_7','pic_8','pic_9','pic_10','pic_11','pic_12','pic_13','pic_14','pic_15','pic_16','pic_17','pic_18','pic_19','pic_20','pic_21','pic_22','pic_23','pic_24','layout_type', )
