from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from examples.models import ExampleTwo


class ExampleTwoChangeForm(ModelForm):
    def clean(self):
        super().clean()
        if self.instance.created_at.date() != timezone.now().date():
            raise ValidationError(
                _('Not editable today'),
                code='expired',
            )

    class Meta:
        model = ExampleTwo
        fields = ('field_one',)
