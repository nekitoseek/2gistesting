import random
import unittest
from get_token_create_favorite import get_token, create_favorite

class TestColor(unittest.TestCase):
    def setUp(self):
        self.cookies = get_token()

    def test_without_color(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": 82.9071}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса без указания color")
        body = resp.json()
        self.assertIsNone(body.get("color"), "Поле color должно быть null, если color не передавался в запросе")

    def test_valid_color(self):
        valid_colors = ['BLUE', 'GREEN', 'RED', 'YELLOW']
        random_valid_color = random.choice(valid_colors)
        data = {"title": "2gis", "lat": 54.98857, "lon": 82.9071, "color": random_valid_color}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 200, "Неверный статус код для запроса с указанием корректного color")
        body = resp.json()
        self.assertEqual(body.get("color"), data["color"], "Поле color не совпадает с отправленным")

    def test_num_in_color(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": 82.9071, "color": "1RED"}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с некорректным color (цифра в color)")

    def test_nonvalidcolor_in_color(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": 82.9071, "color": "PINK"}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с некорректным color (цвет не входящий в перечень)")

    def test_lowercase_color(self):
        data = {"title": "2gis", "lat": 54.98857, "lon": 82.9071, "color": "yellow"}
        resp = create_favorite(data, cookies=self.cookies)
        self.assertEqual(resp.status_code, 400, "Неверный статус код для запроса с некорректным color (нижний регистр)")