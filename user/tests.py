from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Auth
# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        test_post = Auth.objects.create(
            author = test_user,
            title = 'Walking at night in Down Town',
            body = 'Nowadays, when you go to downtown, dont forget to wear your mask or Habiba wont let you in'
        )
        test_post.save() # Save the object to mock Database

    def test_blog_content(self):
        post = Auth.objects.get(id=1)
        actual_author = str(post.author)
        actual_title = str(post.title)
        actual_body = str(post.body)
        self.assertEqual(actual_author, 'testuser')
        self.assertEqual(actual_title, 'Walking at night in Down Town')
        self.assertEqual(actual_body, 'Nowadays, when you go to downtown, dont forget to wear your mask or Habiba wont let you in')

