from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ("first_name", "last_name", "email")


class PositiveIntegerField(forms.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs["min_value"] = 0
        kwargs["validators"] = [self.validate_positive]
        super().__init__(*args, **kwargs)

    def validate_positive(self, value):
        if value < 0:
            raise forms.ValidationError("Please enter positive value.")


class TriangleForm(forms.Form):
    cathetus1 = PositiveIntegerField()
    cathetus2 = PositiveIntegerField()
