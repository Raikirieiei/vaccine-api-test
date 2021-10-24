import unittest
import requests

URL = "https://flamxby.herokuapp.com/"

class TestAPI(unittest.TestCase):

    data =[
        {
            "name":"foo",
            "surname":"rockmakmak",
            "birth_date":"2002-10-22",
            "citizen_id":"1234567848204",
            "occupation":"programmer",
            "address":"bkk thailand",
            "password":"1234",
            "reservations":[
                {
                    "reservation_id":6,
                    "register_timestamp":"2021-10-23T06:44:25.849000"
                },
                {
                    "reservation_id":7,
                    "register_timestamp":"2021-10-20T17:12:39.738000"
                },
                {
                    "reservation_id":8,
                    "register_timestamp":"2021-10-20T17:12:39.738000"
                },
                {
                    "reservation_id":9,
                    "register_timestamp":"2021-10-20T17:12:39.738000"
                },
                {
                    "reservation_id":10,
                    "register_timestamp":"2021-10-20T17:12:39.738000"
                },
                {
                    "reservation_id":3,
                    "register_timestamp":"2021-10-20T17:12:39.738000"
                }
            ]
        }
    ]

    def test_get_user_data(self):
        endpoint = URL + f"user/{self.data[0]['citizen_id']}"
        response = requests.get(endpoint)
        json_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual("foo", json_data['name'] )
        self.assertEqual("rockmakmak", json_data['surname'] )
        self.assertEqual("1234567848204", json_data['citizen_id'] )
        self.assertEqual("programmer", json_data['occupation'] )
        self.assertEqual("bkk thailand", json_data['address'] )
    
    def test_user_not_exist(self):
        endpoint = URL + f"user/111111111111111"
        response = requests.get(endpoint)
        self.assertEqual(404, response.status_code)


    def test_get_reservation_data(self):
        endpoint = URL + f"reservation"
        response = requests.get(endpoint)
        self.assertEqual(200, response.status_code)
        self.assertEqual("application/json", response.headers["Content-Type"])

    def test_get_reservation_data_id(self):
        endpoint = URL + f"reservation/{self.data[0]['reservations'][0]['reservation_id']}"
        response = requests.get(endpoint)
        json_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(6, json_data['reservation_id'] )
        self.assertEqual("2021-10-23T06:44:25.849000", json_data['register_timestamp'] )

    def test_get_reservation_data_by_date(self):
        endpoint = URL + f"reservation/2021/10/20"
        response = requests.get(endpoint)
        json_data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue('foo' in name for name in json_data) 

    def test_reservation_date_not_exist(self):
        endpoint = URL + f"reservation/20000/00/00"
        response = requests.get(endpoint)
        self.assertEqual(404, response.status_code)  
        


if __name__ == "__main__":
     unittest.main()