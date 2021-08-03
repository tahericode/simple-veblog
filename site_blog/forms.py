from django import forms


class Comment_form(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Your name','class':'form-control'}),
    )

    email =forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'Your Email','class':'form-control'}),
    )

   
    comment = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':'Enter your message here','class':'form-control','rows':'6'}),
        
    )