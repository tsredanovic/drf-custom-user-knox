from django.contrib import admin
from django.forms import ModelForm

from examples.forms import ExampleTwoChangeForm
from examples.models import ExampleTwo


class ExampleTwoAdmin(admin.ModelAdmin):
    model = ExampleTwo

    list_display = ('id', 'field_one', )
    list_display_links = ('id',)
    search_fields = ('field_one',)
    ordering = ('field_one',)

    add_form = ModelForm
    add_fieldsets = (
        ('General', {
            'fields': ('field_one', )
        }),
    )

    form = ExampleTwoChangeForm
    fieldsets = (
        ('General', {
            'fields': ('field_one', )
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during instance creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)


admin.site.register(ExampleTwo, ExampleTwoAdmin)
