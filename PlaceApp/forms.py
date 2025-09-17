from django import forms
class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description', 'place_type', 'location', 'rating']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'place_type': forms.TextInput(),
            'location': forms.TextInput(),
        }
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.strip():
            raise forms.ValidationError("Name cannot be empty")
        return name
    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be from 1 to 5")
        return rating
    def clean_place_type(self):
        place_type = self.cleaned_data['place_type']
        if place_type and not place_type.strip():
            return None
        return place_type

