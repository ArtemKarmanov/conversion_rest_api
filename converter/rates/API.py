import requests
from converter.settings import RAPID_API_KEY, RAPID_API_HOST


url = "https://currency-converter-by-api-ninjas.p.rapidapi.com/v1/convertcurrency"

headers = {
	"X-RapidAPI-Key": RAPID_API_KEY,
	"X-RapidAPI-Host": RAPID_API_HOST
}


def get_convert_api(from_currency: str, to_currency: str, amount: str) -> int:
	"""
	Результат конвертации введённой суммы между валютами от API.

	:param from_currency: Из валюты
	:param to_currency: В валюту
	:param amount: Сумма
	:return: response.json()
	"""
	querystring = {"have":from_currency,"want":to_currency,"amount":amount}
	response = requests.get(url, headers=headers, params=querystring)

	# Проверка на успешность запроса
	if response.ok:
		result = response.json()['new_amount']

		return result
	else:

		return False
