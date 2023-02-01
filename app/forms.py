from django import forms
g=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('java','JAVA'),('django','DJANGO')]


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField(min_value=5)
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':10,'rows':10}))