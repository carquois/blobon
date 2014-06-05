# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, Textarea, TextInput, CharField, URLField, ImageField, ModelMultipleChoiceField, EmailField
from django.utils.translation import ugettext_lazy as _
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.db import models

from blogs.models import Blog, Post, Category, Subscription, Info_email, Comment, Page, Rss, Tag


FREQ = (
    ('15m', '15m'),
    ('30m', '30m'),
    ('1h', '1h'),
    ('3h', '3h'),
    ('6h', '6h'),
    ('12h', '12h'),
    ('24h', '24h'),
)

HOURS = (
    ('00:00', '00:00'),
    ('01:00', '01:00'),
    ('02:00', '02:00'),
    ('03:00', '03:00'),
    ('04:00', '04:00'),
    ('05:00', '05:00'),
    ('06:00', '06:00'),
    ('07:00', '07:00'),
    ('08:00', '08:00'),
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    ('11:00', '11:00'),
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
    ('22:00', '22:00'),
    ('23:00', '23:00'),
)



class PageForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Enter your page title'),
                                                    'type': 'text',
                                                    'class': "form-control"}))

    content = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Your page content here'),
                                                    'type': 'text',
                                                    'rows': '10',
                                                    'class': "form-control setting_form input-block-level mceEditor",
                                                    }))
 
    class Meta:
        model = Page
        fields = ('title', 'content', 'status' )

class BlogForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Enter your title'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    slug = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog adress'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    moderator_email = EmailField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Enter the blog moderator email here'),
                                                    'type': 'text',
                                                    'class': "form-control input-block-level"}))
    class Meta:
        model = Blog 
        fields = ('title', 'slug','moderator_email')

class SubmitForm(ModelForm):
    title = CharField(label=_('Title :'), widget=forms.TextInput(attrs={'placeholder': _('Enter your title here.'), 'class': 'form-control'}), required=False)
    translated_title = CharField(label=_('Title translated :'), widget=forms.TextInput(attrs={'placeholder': _('Enter your translation here.'), 'class': 'form-control'}), required=False)
    source = URLField(label=_('Source :'), widget=forms.HiddenInput(), required=False)
    content = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Enter your content here'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control input-block-level mceNoEditor"}))
    translated_content = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Enter your translation here'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control input-block-level mceNoEditor"}))
    message = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Enter your message here'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control input-block-level mceNoEditor"}))
    class Meta:
        model = Post
        fields = ('title', 'translated_title', 'content', 'translated_content', 'message',)





class CommentForm(ModelForm):
    name = CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Your name'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    }))
    comment = CharField(required=True, widget=forms.Textarea(attrs={'placeholder': _('Leave your comment here'),
                                                    'type': 'text',
                                                    'rows': '3',
                                                    'class': "form-control setting_form input-block-level"}))
    email = EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Enter your email here'),
                                                    'type': 'text',
                                                    'class': "form-control input-block-level"}))
    website = URLField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Your website url here'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    occupation = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Your occupation here'),
                                                    'type': 'text',
                                                    'class': "form-control"}))
    class Meta:
        model = Comment
        fields = ('name', 'comment', 'email', 'website', 'occupation' )

class SettingsForm(ModelForm):
    title = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog title'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    slug = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your blog adress'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    password = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Your blog password'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    custom_domain = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Your custom domain'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    description = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Describe Your Blog'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level mceNoEditor"}))    
    short_description = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Describe Your Blog'),
                                                    'type': 'text',
                                                    'rows': '2',
                                                    'class': "form-control setting_form input-block-level mceNoEditor"}))

    main_color = CharField(required=True, widget=forms.TextInput(attrs={'readonly':'readonly', 'placeholder': _('Your blog main color'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    main_image = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_30(this);"}))
    
    pinterest_link = URLField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Link to your Pinterest page here'),
                                                    'type': 'text',
                                                    'class': "form-control"}))

    facebook_link = URLField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Link to your Facebook page here'),
                                                    'type': 'text',
                                                    'class': "form-control"}))

    twitter_link = URLField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Link to your Twitter page here'),
                                                    'type': 'text',
                                                    'class': "form-control"}))    
    analytics_account = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Your Google Analytics account number'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))

    class Meta:
        model = Blog 
        fields = ('pinterest_link','facebook_link', 'twitter_link', 'analytics_account', 'exclusion_start', 'exclusion_end', 'frequency', 'title', 'slug', 'main_color', 'main_image', 'password', 'custom_domain','description','is_online','is_open','short_description','draft_notice' )

class PasswordForm(ModelForm):
    password = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Enter the blog password'),
                                                    'type': 'text',
                                                    'class': "form-control input-block-level"}))
    class Meta:
        model = Blog
        fields = ('password', )
class SubscriptionForm(ModelForm):
    email = EmailField(widget=forms.TextInput(attrs={'placeholder': _('Enter email here'),
                                                    'type': 'text',
                                                    'class': "form-control input-block-level submail"
                                                    }))
    class Meta:
        model = Subscription
        fields = ('email', )


class RssForm(ModelForm):
    feed_url = URLField(widget=forms.TextInput(attrs={'placeholder': _('Enter feed url here'),
                                                    'type': 'text',
                                                    'class': "form-control input-block-level"
                                                    }))
    class Meta:
        model = Rss
        fields = ('feed_url', )


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': _('Your subject here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': _('Enter your message here'),
                                                    'type': 'text',
                                                    'rows': '3',
                                                    'class': "form-control input-block-level"}))
    from_email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': _('Enter your email here'),
                                                    'type': 'text',
                                                    'class': "form-control input-block-level"}))
    cc_myself = forms.BooleanField(required=False)

class EmailForm(ModelForm):
    name = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your campaign name here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    subject = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your subject'),
                                                    'type': 'text',
                                                    'rows': '1',
                                                    'class': "form-control setting_form input-block-level"}))
    message = CharField(widget=forms.Textarea(attrs={'placeholder': _('Your message'),
                                                    'type': 'text',
                                                    'rows': '10',
                                                    'class': "form-control setting_form input-block-level mceNoEditor"}))
    class Meta:
        model = Info_email
        fields = ('name','subject','message','subscribers','frequency', )

class TagsForm(ModelForm):
    name = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your tag name here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    description = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Describe your tag'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level mceNoEditor"}))
    slug = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Slug'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))

    class Meta:
        model = Tag
        fields = ('name','slug','description',)


class CategoriesForm(ModelForm):
    name = CharField(widget=forms.TextInput(attrs={'placeholder': _('Your category name here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    description = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Describe your category'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level mceNoEditor"}))
    slug = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Slug'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    color = CharField(required=True, widget=forms.TextInput(attrs={'readonly':'readonly', 'placeholder': _('Your category color'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level"}))
    class Meta:
        model = Category
        exclude=('author', ' parent_category',)
        fields = ('name','description','slug','color','parent_category', )
    def __init__(self, *args, **kwargs):
        blog = kwargs.pop('blog', None)
        super(CategoriesForm, self).__init__(*args, **kwargs)
        if blog:
            self.fields['parent_category'].queryset = Category.objects.filter(blog=blog)



class PostForm(ModelForm):
    title = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Write your title here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    }))
    temp_tag_field = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Write your tag name or tags separated by commas'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    translated_title = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Write your translated title here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    source = URLField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Your source'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    }))
    artist = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Write artist name here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    }))
    content = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write a new post'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level mceNoEditor",
                                                    }))
    text = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write your text here'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level mceNoEditor",
                                                    }))
    category = ModelMultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all())
    tag = ModelMultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, queryset=Tag.objects.all())
    content_0 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '10',
                                                    'class': "form-control setting_form input-block-level mceEditor",
                                                    }))
    content_01 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level mceNoEditor",
                                                    'autofocus':'on'}))
    content_1 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev mceNoEditor",
                                                    'autofocus':'on'}))
    content_2 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev mceNoEditor",
                                                    'autofocus':'on'}))
    content_3 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev mceNoEditor",
                                                    'autofocus':'on'}))
    content_4 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev mceNoEditor",
                                                    'autofocus':'on'}))
    content_5 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev mceNoEditor",
                                                    'autofocus':'on'}))
    content_6 = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this image'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control setting_form input-block-level smallprev mceNoEditor",
                                                    'autofocus':'on'}))
    content_video = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Write something about this video'),
                                                    'type': 'text',
                                                    'rows': '3',
                                                    'class': "form-control setting_form input-block-level mceNoEditor",
                                                    'autofocus':'on'}))
    translated_content = CharField(required=False, widget=forms.Textarea(attrs={'placeholder': _('Enter your translation here'),
                                                    'type': 'text',
                                                    'rows': '5',
                                                    'class': "form-control input-block-level mceNoEditor"}))
    video_url = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Youtube or Vimeo url here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    soundcloud_url = CharField(required=False, widget=forms.TextInput(attrs={'placeholder': _('Soundcloud playlist url here'),
                                                    'type': 'text',
                                                    'class': "form-control setting_form input-block-level",
                                                    'autofocus':'on'}))
    pic = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_0(this);"}))
    pic_1 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_1(this);"}))
    pic_2 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_2(this);"}))
    pic_3 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_3(this);"}))
    pic_4 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_4(this);"}))
    pic_5 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_5(this);"}))
    pic_6 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_6(this);"}))
    pic_7 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_7(this);"}))
    pic_8 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_8(this);"}))
    pic_9 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_9(this);"}))
    pic_10 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_10(this);"}))
    pic_11 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_11(this);"}))
    pic_12 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_12(this);"}))
    pic_13 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_13(this);"}))
    pic_14 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_14(this);"}))
    pic_15 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_15(this);"}))
    pic_16 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_16(this);"}))
    pic_17 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_17(this);"}))
    pic_18 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_18(this);"}))
    pic_19 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_19(this);"}))
    pic_20 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_20(this);"}))
    pic_21 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_21(this);"}))
    pic_22 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_22(this);"}))
    pic_23 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_23(this);"}))
    pic_24 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_24(this);"}))
    pic_25 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_25(this);"}))
    pic_26 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_26(this);"}))
    pic_27 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_27(this);"}))
    pic_28 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_28(this);"}))
    pic_29 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_29(this);"}))
    pic_30 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_30(this);"}))
    pic_31 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_31(this);"}))
    pic_32 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_32(this);"}))
    pic_33 = ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange':"upload_img_33(this);"}))
    is_ready = forms.BooleanField(required=False) 
    class Meta:
        model = Post
        exclude=('author',' category',) 
        fields = ('tag','soundcloud_id','soundcloud_url','is_sticky', 'youtube_id','title','content','source','status','artist','text','translated_title','is_ready','translated_content','content_0','content_01','content_1','content_2','content_3','content_4','content_5','content_6','content_video', 'pic','pic_0','pic_04','pic_1','pic_2','pic_3','pic_4','pic_5','pic_6','video_url','category',
'pic_7','pic_8','pic_9','pic_10','pic_11','pic_12','pic_13','pic_14','pic_15','pic_16','pic_17','pic_18','pic_19','pic_20','pic_21','pic_22','pic_23',
'pic_24','pic_25','pic_26','pic_27','pic_28','pic_29','pic_30','pic_31','pic_32','pic_33','layout_type','temp_tag_field', )
    def __init__(self, *args, **kwargs):
        blog = kwargs.pop('blog', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if blog:
            self.fields['category'].queryset = Category.objects.filter(blog=blog)
            self.fields['tag'].queryset = Tag.objects.filter(blog=blog)
