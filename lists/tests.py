from django.urls import resolve
from django.test import TestCase
from  lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTest(TestCase):


    def test_home_page_returns_correct_html(self):
        #instead of creating httprequenst and calling the view function
        #we call self.client.get , passing it the URL we want to test
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
