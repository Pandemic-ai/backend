
import json
import os
from rest_framework.generics import GenericAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView


class StubMixin:
    def get_stub_name(self, request):
        if hasattr(self, 'stub_name'):
            return self.stub_name
        parts = request.path.strip('/').split('/')
        for i, part in enumerate(parts[2:]):
            if part.isnumeric():
                parts[i + 2] = 'N'
        return '_'.join(parts)

    def get(self, request, **kwargs):
        filename = self.get_stub_name(request) + '.json'
        with open(os.path.join(os.path.dirname(__file__), 'stubs', filename)) as f:
            resp = json.load(f)
        return Response(resp)


class StubView(StubMixin, APIView):
    pass
