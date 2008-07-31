from django import forms
from django.contrib.auth.models import User

from intranet.org.models import TipSodelovanja, Person, Event, Sodelovanje
from intranet.org.models import Bug, Resolution, Clipping



class EventForm(forms.ModelForm):
    class Meta:
        model = Event

class FilterBug(forms.Form):
    resolution = forms.ModelChoiceField(Resolution.objects.all(), required=False)
    #assign = forms.ModelChoiceField(User.objects.all(), required=False, widget=forms.SelectMultiple)
    ##there's gotta be a better way to do this
    ids = []
    for u in User.objects.all():
        ids += [(u.id, u)]

    #assign = forms.MultipleChoiceField(ids, required=False)
    assign = forms.ModelChoiceField(User.objects.all(), required=False)
    author = forms.ModelChoiceField(User.objects.all(), required=False)

    due_by = forms.DateTimeField(required=False)

    name = forms.CharField(required=False)

class BugForm(forms.ModelForm):
    class Meta:
        exclude = ('resolved', 'tags', 'author',)
        model = Bug

class CommentBug(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class SodelovanjeFilter(forms.ModelForm):
    ##override the person in 'Sodelovanje', as there is required
    person = forms.ModelChoiceField(Person.objects.all(), required=False)
    c = [('', '---------'), ('txt', 'txt'), ('pdf', 'pdf'), ('csv', 'csv')]
    export = forms.ChoiceField(choices=c, required=False)

    class Meta:
        model = Sodelovanje

class ClippingFilter(forms.ModelForm):
    class Meta:
        model = Clipping
