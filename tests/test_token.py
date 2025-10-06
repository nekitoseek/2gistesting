import unittest
import time
from get_token_create_favorite import get_token, create_favorite

class TestToken(unittest.TestCase):
    def test_without_token(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies={})
        self.assertEqual(resp.status_code, 401, "Неверный статус код для запроса без токена")

    def test_expired_token(self):
        cookies = get_token()
        time.sleep(2)
        data = {"title": "2gis", "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=cookies)
        self.assertEqual(resp.status_code, 401, "Неверный статус код для запроса с просроченным токеном")