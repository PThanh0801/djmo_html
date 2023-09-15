from django import forms
from Phuc_App.models import Baibao

class BaibaoForm(forms.ModelForm):
    class Meta:
        model = Baibao
        fields = ['title', 'content', 'image']
        widgets = { 'title':forms.TextInput(attrs={'class':'form-control'}),
                'content':forms.Textarea(attrs={'class':'form-control'}),
                'image':forms.URLInput(attrs={'class':'form-control'}),
        }