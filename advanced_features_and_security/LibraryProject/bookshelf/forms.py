from django import forms

class ExampleForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=True,
        label="Search",
        widget=forms.TextInput(attrs={'placeholder': 'Enter book title or keyword'})
    )
