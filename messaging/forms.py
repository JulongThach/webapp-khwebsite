from django import forms

class MessageForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput, label="Name")
    phone = forms.CharField(widget=forms.TextInput, label="Phone Number")
    subject = forms.CharField(widget=forms.TextInput, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")