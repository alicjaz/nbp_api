from datetime import datetime

import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def avg_exchange_rate(request, currency_code, date):
    url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{date}/?format=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        average_rate = data['rates'][0]['mid']
        return JsonResponse({'average_exchange_rate': average_rate})
    else:
        return JsonResponse({'error': 'Unable to retrieve data from NBP API'}, status=500)


@require_http_methods(['GET'])
def min_max_average(request, currency_code, n):
    if request.method == 'GET':
        url = f'https://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/last/{n}/?format=json'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()['rates']

            # Initialize variables to hold daily average values
            averages = {}
            for i in range(n):
                date = datetime.strptime(data[i]['effectiveDate'], '%Y-%m-%d').date()
                averages[date] = {'sum': 0, 'count': 0}

            # Calculate daily average values
            for i in range(n):
                date = datetime.strptime(data[i]['effectiveDate'], '%Y-%m-%d').date()
                bid = data[i]['mid']
                averages[date]['sum'] += bid
                averages[date]['count'] += 1

            # Calculate min and max daily average values
            min_average = None
            max_average = None
            min_average_dates = None
            max_average_dates = None
            for date in averages:
                average = averages[date]['sum'] / averages[date]['count']
                if min_average is None or average < min_average:
                    min_average = average
                    min_average_dates = date.strftime('%Y-%m-%d')
                if max_average is None or average > max_average:
                    max_average = average
                    max_average_dates = date.strftime('%Y-%m-%d')

            # Return the result as a JSON response
            return JsonResponse({
                'currency': currency_code,
                'n': n,
                'min_average': min_average,
                'min_average_dates': min_average_dates,
                'max_average': max_average,
                'max_average_dates': max_average_dates
            })
        else:
            # If the API returned an error status code, return an error message as a JSON response
            return JsonResponse({'error': f'API returned status code {response.status_code}'},
                                status=response.status_code)

    # If the request method is not GET, return an error message as a JSON response
    return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)


@require_http_methods(['GET'])
def buy_sell_difference(request, currency_code, n):
    if request.method == 'GET':
        url = f"https://api.nbp.pl/api/exchangerates/rates/c/{currency_code}/last/{n}/?format=json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            rates = data["rates"]
            differences = {}
            for rate in rates:
                date = rate["effectiveDate"]
                ask_rate = rate["ask"]
                bid_rate = rate["bid"]
                difference = ask_rate - bid_rate
                differences[date] = difference

            max_difference_date = max(differences, key=differences.get)
            min_difference_date = min(differences, key=differences.get)

            return JsonResponse({
                "max_difference_date": max_difference_date,
                "max_difference": differences[max_difference_date],
                "min_difference_date": min_difference_date,
                "min_difference": differences[min_difference_date]
            })
        else:
            return JsonResponse({"error": "Error retrieving data from NBP API."}, status=500)
    else:
        return JsonResponse({"error": "Invalid HTTP method."}, status=405)
