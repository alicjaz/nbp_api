from django.test import TestCase, Client
from django.urls import reverse


# Test case for average exchange rate API
class AvgExchangeRateTestCase(TestCase):
    def setUp(self):
        # Create a test client
        self.client = Client()

    # Test the average exchange rate API
    def test_avg_exchange_rate(self):
        # Set the input parameters
        date = '2023-04-25'
        currency_code = 'USD'
        expected_keys = ['average_exchange_rate']

        # Call the API endpoint with the given parameters
        url = reverse('avg_exchange_rate', kwargs={'date': date, 'currency_code': currency_code})
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Parse the response JSON data
        data = response.json()
        # Assert that the expected keys are present in the response data
        for key in expected_keys:
            self.assertIn(key, data)
        # Assert that the average exchange rate value is of float type
        self.assertIsInstance(data['average_exchange_rate'], float)

# Test case for min max average API
class MinMaxAverageTestCase(TestCase):
    def setUp(self):
        # Create a test client
        self.client = Client()
        # Set the default input parameters for the API
        self.currency_code = 'USD'
        self.n = 5
        # Set the expected keys for the response JSON data
        self.expected_keys = ['currency', 'n', 'min_average', 'min_average_dates', 'max_average', 'max_average_dates']

    # Test the min max average API
    def test_min_max_average(self):
        # Call the API endpoint with the default input parameters
        url = reverse('min_max_average', args=[self.currency_code, self.n])
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Parse the response JSON data
        data = response.json()
        # Assert that the expected keys are present in the response data
        for key in self.expected_keys:
            self.assertIn(key, data)


# Test case for buy sell difference API
class BuySellDifferenceTestCase(TestCase):
    def setUp(self):
        # Create a test client to simulate HTTP requests
        self.client = Client()
        # Set the default input parameters for the API
        self.currency_code = 'USD'
        self.n = 5

    def test_buy_sell_difference(self):
        # Construct the URL for the API endpoint with the input parameters
        url = reverse('buy_sell_difference', args=[self.currency_code, self.n])
        # Send a GET request to the API endpoint with the constructed URL
        response = self.client.get(url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Convert the response data from JSON to a Python dictionary
        data = response.json()
        # Check if the dictionary contains the expected keys
        self.assertIn('max_difference_date', data)
        self.assertIn('max_difference', data)
        self.assertIn('min_difference_date', data)
        self.assertIn('min_difference', data)
