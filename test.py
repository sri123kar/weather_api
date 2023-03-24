import unittest
import requests

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:5000" # API base URL
        self.station_code = "USC00110072" # Valid station code
        self.date = "1985-01-01" # valid date
        self.year = 1985
        self.endpoint = f"/api/weather/{self.station_code}/{self.date}"
        
    def test_successful_request(self):
        response = requests.get(self.base_url + self.endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())
        
    def test_invalid_station_code_date(self):
        invalid_station_code = "XYZ" #  invalid station code
        endpoint = f"/api/weather/{invalid_station_code}/{self.date}"
        response = requests.get(self.base_url + endpoint)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "Station code not found or date is incorrect"})

    def test_invalid_date(self):
        invalid_date = "2022-13-32" # Replace with invalid date
        endpoint = f"/api/weather/{self.station_code}/{invalid_date}"
        response = requests.get(self.base_url + endpoint)
        self.assertEqual(response.status_code, 500)


    def test_successful_request_for_stats_data(self):
        endpoint = f"/api/weather/stats/{self.station_code}/{self.year}"
        print(self.base_url + self.endpoint)
        response = requests.get(self.base_url + endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.json())



    def test_invalid_station_code_date_for_stats_data(self):
        invalid_station_code = "XYZ" #  invalid station code
        endpoint = f"/api/weather/stats/{invalid_station_code}/{self.year}"
        response = requests.get(self.base_url + endpoint)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "Station code not found or date is incorrect"})

    def test_invalid_date_for_stats_data(self):
        invalid_year = "00000" # Replace with invalid date
        endpoint = f"/api/weather/stats/{self.station_code}/{invalid_year}"
        response = requests.get(self.base_url + endpoint)
        self.assertEqual(response.status_code, 404)

        
if __name__ == '__main__':
    unittest.main()

