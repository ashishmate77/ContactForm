from django import forms

class EmpForm(forms.Form):
    ename = forms.CharField(
        label = "Enter Name",
        widget = forms.TextInput(
            attrs = {
                'class':'Form-control',
                'placeholder':'Enter Name Here'
            }
        )
    )

    salary = forms.IntegerField(
        label = "Enter Salary",
        widget = forms.NumberInput(
            attrs = {
                'class':'Form-control',
                'placeholder':'Enter your salary'
            }
        )
    )

    email = forms.EmailField(
        label = "Enter Email Id ",
        widget = forms.EmailInput(
            attrs = {
                'class':'Form-control',
                'placeholder':'Email ID here'
            }
        )
    )

    mobile = forms.IntegerField(
        label = "Mobile Number",
        widget = forms.NumberInput(
            attrs = {
                'class':'Form-control',
                'placeholder':'Your mobile number'
            }
        )
    )

    location = forms.CharField(
        label = "Location",
        widget = forms.TextInput(
            attrs = {
                'class':'Form-control',
                'placeholder':'Enter Your Location'
            }
        )
    )