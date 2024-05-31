# planning/forms.py

from django import forms
from .models import UrbanPlanningRecord
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Row, Column

class UrbanPlanningRecordForm(forms.ModelForm):
    class Meta:
        model = UrbanPlanningRecord
        fields = ['title', 'description', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the title of the record', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter a detailed description', 'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter the location', 'class': 'form-control'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(UrbanPlanningRecordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Record Details',
                Row(
                    Column('title', css_class='form-group col-md-6 mb-0'),
                    Column('location', css_class='form-group col-md-6 mb-0'),
                    css_class='form-row'
                ),
                'description'
            ),
            Submit('submit', 'Save', css_class='btn btn-primary')
        )

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError('Title must be at least 5 characters long.')
        return title

    def clean_location(self):
        location = self.cleaned_data.get('location')
        if len(location) < 3:
            raise forms.ValidationError('Location must be at least 3 characters long.')
        return location
