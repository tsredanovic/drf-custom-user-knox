from rest_framework import serializers, exceptions

from examples.models import ExampleOne


class ExampleOneSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        field_one = attrs.get('field_one')
        field_two = attrs.get('field_two')
        user = self.context['request'].user

        combination_exists = ExampleOne.objects.filter(field_one=field_one, field_two=field_two, last_edit_by=user).exists()

        if combination_exists:
            raise exceptions.ValidationError('Combination already exists.')

        return attrs

    class Meta:
        model = ExampleOne
        fields = '__all__'
        read_only_fields = ('id', 'last_edit_by')
