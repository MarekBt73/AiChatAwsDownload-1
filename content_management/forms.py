from django import forms
from .models import EducationalMaterial, Video, Article, Ebook

class EducationalMaterialForm(forms.ModelForm):
    class Meta:
        model = EducationalMaterial
        fields = ['title', 'description', 'material_type', 'subject', 'difficulty_level', 'content']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'url', 'subject', 'difficulty_level']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'content', 'subject', 'difficulty_level']

class EbookForm(forms.ModelForm):
    class Meta:
        model = Ebook
        fields = ['title', 'description', 'file', 'subject', 'difficulty_level']
