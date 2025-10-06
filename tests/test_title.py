import unittest
from get_token_create_favorite import get_token, create_favorite

class TestTitle(unittest.TestCase):
    def setUp(self):
        self.cookies = get_token()

    def test_valid_title(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для валидных значений")
        body = resp.json()
        self.assertEqual(body.get("title"), data["title"], "Поле title не совпадает с отправленным")
        self.assertEqual(body.get("lat"), data["lat"], "Поле lat не совпадает с отправленным")
        self.assertEqual(body.get("lon"), data["lon"], "Поле lon не совпадает с отправленным")

    def test_miss_title(self):
        data = {"lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с отсутствующим title")

    def test_empty_title(self):
        data = {"title": "", "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с пустым title")

    def test_1char_title(self):
        data = {"title": "W", "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с разрешенным количеством символов(1) в title")
        body = resp.json()
        self.assertEqual(body.get("title"), data["title"], "Поле title не совпадает с отправленным")

    def test_499chars_title(self):
        data = {"title": "W"*499, "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с разрешенным количеством символов(499) в title")
        body = resp.json()
        self.assertEqual(body.get("title"), data["title"], "Поле title не совпадает с отправленным")

    def test_999chars_title(self):
        data = {"title": "W" * 999, "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с разрешенным количеством символов(999) в title")
        body = resp.json()
        self.assertEqual(body.get("title"), data["title"], "Поле title не совпадает с отправленным")

    def test_1000chars_title(self):
        data = {"title": "W"*1000, "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с количеством символов, выходящих за рамки допустимого в title")

    def test_latin_in_title(self):
        data = {"title": "NSK", "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с латиницей")
        body = resp.json()
        self.assertEqual(body.get("title"), data["title"], "Поле title не совпадает с отправленным")

    def test_cyrillic_in_title(self):
        data = {"title": "НСК", "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с латиницей")
        body = resp.json()
        self.assertEqual(body.get("title"), data["title"], "Поле title не совпадает с отправленным")

    def test_number_in_title(self):
        data = {"title": "1234567890", "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с цифрами")
        body = resp.json()
        self.assertEqual(body.get("title"), data["title"], "Поле title не совпадает с отправленным")

    def test_symbols_in_title(self):
        data = {"title": "?.,!@", "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с знаками препинания")
        body = resp.json()
        self.assertEqual(body.get("title"), data["title"], "Поле title не совпадает с отправленным")