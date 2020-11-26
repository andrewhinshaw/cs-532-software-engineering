from django.test import TestCase
from django.urls import reverse
# from django.test import SimpleTestCase
from .models import Order


# Create your tests here.
# class PageTests(SimpleTestCase):
#     def test_home_page_status_code(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#
#     def test_about_page_status_code(self):
#         response = self.client.get('/about/')
#         self.assertEqual(response.status_code, 200)

class OrderModelTest(TestCase):

    def setUp(self):
        Order.objects.create(name='test name')

    def test_text_content(self):
        order=Order.objects.get(id=1)
        expected_object_name = f'{order.name}'
        self.assertEqual(expected_object_name, 'test name')

class HomePageViewTest(TestCase):

    def setUp(self):
        Order.objects.create(name='another test name')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
