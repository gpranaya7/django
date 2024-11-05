from django import forms

def valid_for_char(data):
    if not data.isalpha():
        raise forms.ValidationError('error')



class StudentForm(forms.Form):
    sname=forms.CharField(validators=[valid_for_char])
    sid=forms.IntegerField()
    semail=forms.EmailField()
    remail=forms.EmailField()
    def clean(self):
        e=self.cleaned_data['semail']
        r=self.cleaned_data['remail']
        if e!=r:
            raise forms.ValidationError('error')


