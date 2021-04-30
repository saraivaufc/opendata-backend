from django import forms
from django.contrib.admin import widgets

from data.models import Task


class TaskForm(forms.ModelForm):
    source_date = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime())

    dataset = forms.ChoiceField(choices=Task.DATASET_CHOICES,
                                disabled=True,
                                required=False)
    source_format = forms.ChoiceField(choices=Task.FORMAT_CHOICES,
                                      disabled=True,
                                      required=False)

    class Meta:
        model = Task
        fields = ['dataset', 'source', 'source_format', 'source_date']
