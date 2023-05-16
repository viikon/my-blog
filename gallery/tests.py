from django.test import TestCase
from gallery.models import Image
from django.core.files import File

# Create your tests here.
class GalleryModelTest(TestCase):

    def test_gallery_model_save_and_retrive(self):
        image_1 = Image(
            title = 'image 1',
            image = File(open('gallery/media/1.jpg', 'r'))
        )
        image_1.save

        image_2 = Image(
            title = 'image 2',
            image = File(open('gallery/media/2.jpeg', 'r'))
        )
        image_2.save

        all_images = Image.objects.all()

        self.assertEqual(len(all_images), 2)

        self.assertEqual(
            all_images[0].title, image_1.title
            )
        
        self.assertEqual(
            all_images[0].image, image_1.image
            )
        
        self.assertEqual(
            all_images[1].title, image_2.title
            )
        
        self.assertEqual(
            all_images[1].image, image_2.image
            )

if __name__=="__main__":
    TestCase.main()