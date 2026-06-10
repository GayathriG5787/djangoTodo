from django import forms
from .models import Task

class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Task
        fields = ['title', 'description']

    def clean_title(self):
        title = self.cleaned_data['title']

        if Task.objects.filter(
            user=self.user,
            title__iexact=title,
            complete=False
        ).exists():
            raise forms.ValidationError(
                "An incomplete task with this title already exists."
            )

        return title