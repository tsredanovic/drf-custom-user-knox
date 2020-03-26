from django.contrib import admin

from examples.forms import ExampleTwoChangeForm
from examples.models import ExampleTwo


class ExampleTwoAdmin(admin.ModelAdmin):
    model = ExampleTwo

    list_display = ('id', 'field_one', )
    list_display_links = ('id',)
    search_fields = ('field_one',)
    ordering = ('field_one',)

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


admin.site.register(ExampleTwo, ExampleTwoAdmin)