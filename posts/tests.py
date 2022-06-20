from django.test import TestCase

# Create your tests here.
from posts.models import Post


class Test(TestCase):
    def setUp(self):
        Post.objects.create(text="just test")

    def test_test_content(self):
        post_get = Post.objects.get(id=1)
        expected_obj_name = f'{post_get.text}'
        self.assertEqual(expected_obj_name, 'just test')


