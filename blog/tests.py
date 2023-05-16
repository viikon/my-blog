
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
#import unittest
from .views import post_list

# Create your tests here.
class HomePageTests(TestCase):

    def test_root_urlpatterns_to_post_list(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)
    

    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<h1><a href="/">JUST AN ART</a></h1>', html)
        self.assertTrue(html.endswith('</html>'))

#class ArticalModelTests(TestCase):



if __name__=="__main__":
    TestCase.main()    
