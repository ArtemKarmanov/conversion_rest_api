from rates.API import get_convert_api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample


@extend_schema(
	summary='Конвертация суммы из одной валюты в другую',
	responses={
		200: OpenApiResponse(
			'Статус ответа ОК',
			description='Успешный запрос.'
		),
		400: OpenApiResponse(
			description='Статус ответа отрицательный. Некорректный запрос.',
		),
	},
	examples=[
		OpenApiExample(
			'Пример',
			value={
				'result': 95.65
			},
			description='Пример результата успешного запроса.',
			status_codes=[200]
		),
	],
	parameters=[
		OpenApiParameter(
			name='from',
			location=OpenApiParameter.QUERY,
			description='От какой валюты должна происходить конвертация.',
			required=True,
			type=str
		),
		OpenApiParameter(
			name='to',
			location=OpenApiParameter.QUERY,
			description='В какую валюту необходимо сделать конвертацию.',
			required=True,
			type=str
		),
		OpenApiParameter(
			name='value',
			location=OpenApiParameter.QUERY,
			description='Сумма, по которой происходит калькуляция по курсу.',
			default='1',
			required=False,
			type=str
		)
	])
class RatesCurrencies(APIView):
	"""
	Сервис по конвертации из одной валюты в другую.
	"""

	def get(self, request: Request) -> Response:
		"""
		Результат конвертации суммы из одной валюты в другую.

		:param request: Запрос
		:return: Response
		"""
		data = self.request.GET
		from_currency = data.get('from')
		to_currency = data.get('to')
		value_convert = data.get('value')

		# Если не указана одна из валют, то ошибка запроса
		if not from_currency or not to_currency:
			return Response(status=status.HTTP_400_BAD_REQUEST)
		# Если не введена сумма для конвертации, то по умолчанию 1
		elif not value_convert:
			value_convert = '1'

		to_amount_result = get_convert_api(
			from_currency=from_currency,
			to_currency=to_currency,
			amount=value_convert,
		)

		# Если от API есть результат, то выводим
		if to_amount_result:
			response = {'result': to_amount_result}

			return Response(data=response, status=status.HTTP_200_OK)
		# Иначе ошибка запроса
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
