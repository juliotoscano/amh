from django import forms

class updateXML(forms.Form):
    lot = forms.FileField(label='Files',widget=forms.ClearableFileInput(attrs={'multiple':True}))