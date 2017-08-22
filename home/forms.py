from django import forms



class ContactForm(forms.Form):
    

    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(required=True, widget=forms.Textarea)