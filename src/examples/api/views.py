from rest_framework import mixins, viewsets

from examples.api.serializers import ExampleOneSerializer
from examples.models import ExampleOne


class ExampleOneViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet,
                        ):
    http_method_names = ['head', 'get', 'post', 'patch']

    queryset = ExampleOne.objects.all()
    serializer_class = ExampleOneSerializer

    def perform_create(self, serializer):
        serializer.save(last_edit_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(last_edit_by=self.request.user)
