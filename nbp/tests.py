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