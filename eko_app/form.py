from django import forms
from django.core.exceptions import ValidationError
from .models import *

class AddSolutionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['man'].empty_label = "не указан"
        self.fields['woman'].empty_label = "не указана"

    class Meta:
        model = Solution
        fields = [
            'number',
            'commission_name',
            'solution',
            'org_referal',
            'reason',
            'commission_chairman',
            'commission_secretary',
            'commission_members',
            'man',
            'woman',
        ]
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-input'}),
            'commission_name': forms.TextInput(attrs={'class': 'form-input'}),
            'solution': forms.Select(attrs={'class': 'form-input'}),
            'org_referal': forms.Select(attrs={'class': 'form-input'}),
            'reason': forms.Textarea(attrs={'class': 'form-input'}),
            'commission_chairman': forms.TextInput(attrs={'class': 'form-input'}),
            'commission_secretary': forms.TextInput(attrs={'class': 'form-input'}),
            'commission_members': forms.Textarea(attrs={'class': 'form-input'}),
            'man': forms.Select(attrs={'class': 'form-input'}),
            'woman': forms.Select(attrs={'class': 'form-input'}),
        }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 200:
    #         raise ValidationError('Длина превышает 200 символов')
    #
    #     return title