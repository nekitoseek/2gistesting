import unittest
from get_token_create_favorite import get_token, create_favorite

class TestDifferent(unittest.TestCase):
    def setUp(self):
        self.cookies = get_token()

    def test_empty_all_fields(self):
        data = {"title": "", "lat": "", "lon": ""}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса, где все значения пусты")