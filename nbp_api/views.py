from django.http import JsonResponse
import requests


def avg_exchange_rate(request, currency_code, date):
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{date}/?format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        average_rate = data['rates'][0]['mid']
        return JsonResponse({'average_exchange_rate': average_rate})
    else:
        return JsonResponse({'error': 'Unable to retrieve data from NBP API'}, status=500)