import unittest
from app import app, read_markdown_file

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_read_markdown_file(self):
        content = read_markdown_file('DATA.md')
        self.assertIsNotNone(content)

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<div class="info-block">', response.data)

if __name__ == '__main__':
    unittest.main()