from django import forms
class PlaceForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False
    )
    place_type = forms.CharField(required=False)
    location = forms.CharField(required=False)
    rating = forms.IntegerField(min_value=1, max_value=5, required=True)

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.strip():
            raise forms.ValidationError("Name cannot be empty")
        return name

    def clean_place_type(self):
        place_type = self.cleaned_data.get('place_type')
        if place_type and not place_type.strip():
            return None
        return place_type

