from django import forms

from what_can_i_cook.models import IngredientGroup


class MyIngModelChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return str(obj.name)


class ChooseIngForm(forms.Form):

    ing_form = MyIngModelChoiceField(queryset=IngredientGroup.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ing_form'].widget.attrs.update({'id': 'choose-ing-form'})
        self.fields['ing_form'].label = ""


    class Media:
        css = {
            'all': ('https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/css/select2.min.css',)
        }
        js = ('https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/js/select2.min.js',)
