from django import forms

from whisky.models import Whisky

class SearchWhiskyForm(forms.Form):
    query = forms.CharField(label='Search', max_length=None, min_length=1)

class CreateWhiskyForm(forms.ModelForm):
    class Meta:
        model = Whisky
        fields = ['name','age','strength','malt','destillery','chill_filtered','coloured']
