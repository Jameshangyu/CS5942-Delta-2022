from django.test import Client, TestCase


# Unit tests.

class pagesTests(TestCase):

#A test to check index page loads and contain correct text
    def test_index_text(self):
        client = Client()
        response = client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Scan A Panel Into A Variogram")


#A test to check results page loads and content has displayed correctly
    def test_result_text(self):
        client = Client()
        response = client.get('/result')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your panel has created")


