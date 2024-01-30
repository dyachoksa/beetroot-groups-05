from django import forms


class ReviewForm(forms.Form):
    content = forms.CharField(
        max_length=1000, widget=forms.Textarea(attrs={"rows": 3}), required=True,
        label="Review"
    )
