from django import forms

class ProcessImageForm(forms.Form):
    # TODO: Define form fields here
    def __init__(self, *args, **kwargs):
        super(ProcessImageForm, self).__init__(*args, **kwargs)
        self.fields['image'] = forms.ImageField(label='Uplaoad an image')
