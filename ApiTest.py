import unittest
import requests

URL = "https://suchonsite-server.herokuapp.com/"

class TestAPI(unittest.TestCase):

    def test_get_all_people_data(self):
        endpoint = URL + f"people/all"
        response = requests.get(endpoint)
        self.assertEquals(response.status_code, 200)

    def test_appointment_by_date(self):
        endpoint = URL + f"people/by_date/20-10-2021"
        response = requests.get(endpoint)
        self.assertEquals(response.status_code, 200)

    def test_appointment_unexisting_date(self):
        endpoint = URL + f"people/by_date/100-000-5000"
        response = requests.get(endpoint)
        self.assertEquals(response.status_code, 404)
    
    def test_appointment_unexisting_url(self):
        endpoint = URL + f"not_existing/page"
        response = requests.get(endpoint)
        self.assertEquals(response.status_code, 404)


if __name__ == "__main__":
     unittest.main()