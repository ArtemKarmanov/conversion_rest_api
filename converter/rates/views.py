from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class RatesCurrencies(APIView):
	def get(self, request: Request) -> Response:
		return Response(data={})
