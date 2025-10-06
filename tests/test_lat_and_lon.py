import unittest
from get_token_create_favorite import get_token, create_favorite

class TestLatAndLon(unittest.TestCase):
    def setUp(self):
        self.cookies = get_token()

    # lat
    def test_miss_lat(self):
        data = {"title": "2gis", "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с пропущенным lat")

    def test_empty_lat(self):
        data = {"title": "2gis", "lat": "", "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с пустым lat")

    def test_minus91_lat(self):
        data = {"title": "2gis", "lat": -91, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с невалидным lat")

    def test_minus90_lat(self):
        data = {"title": "2gis", "lat": -90, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с валидным lat")
        body = resp.json()
        self.assertEqual(body.get("lat"), data["lat"], "Поле lat не совпадает с отправленным")

    def test_90_lat(self):
        data = {"title": "2gis", "lat": 90, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с валидным lat")
        body = resp.json()
        self.assertEqual(body.get("lat"), data["lat"], "Поле lat не совпадает с отправленным")

    def test_91_lat(self):
        data = {"title": "2gis", "lat": 91, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с невалидным lat")

    def test_nonum_lat(self):
        data = {"title": "2gis", "lat": "2gis", "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с нечисловым lat")

    # lon
    def test_miss_lon(self):
        data = {"title": "2gis", "lat": 54.98857}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с пропущенным lon")

    def test_empty_lon(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": ""}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с пустым lon")

    def test_minus181_lon(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": -181}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с невалидным lon")

    def test_minus180_lon(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": -180}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с валидным lon")
        body = resp.json()
        self.assertEqual(body.get("lon"), data["lon"], "Поле lon не совпадает с отправленным")

    def test_180_lon(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": 180}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с валидным lon")
        body = resp.json()
        self.assertEqual(body.get("lon"), data["lon"], "Поле lon не совпадает с отправленным")

    def test_181_lon(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": 181}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с невалидным lon")

    def test_nonum_lon(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": "2gis"}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с нечисловым lon")

    # lat and lon
    def test_zero_lat_lon(self):
        data = {"title": "2gis", "lat": 0, "lon": 0}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с валидными lat и lon (0, 0)")
        body = resp.json()
        self.assertEqual(body.get("lat"), data["lat"], "Поле lat не совпадает с отправленным")
        self.assertEqual(body.get("lon"), data["lon"], "Поле lon не совпадает с отправленным")