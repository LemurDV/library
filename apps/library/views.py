from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class ModelAPIView(APIView):
    def get(self, request) -> Response:
        return Response("sosok")
