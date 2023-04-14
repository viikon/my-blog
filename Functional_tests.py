from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class BasicInstallTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_ClickPost(self):
        #в браузере открывается сайт, имя вкладки в браузере 'JUST AN ART'
        self.driver.get("http://127.0.0.1:8000/")
        self.assertIn('JUST AN ART', self.driver.title)
        #self.fail("Finish the tests")

    def test_FindHeader(self):
        #проверка заголовка/шапки сайта в браузере "JUST AN ART"
        self.driver.get("http://127.0.0.1:8000/")
        #header = self.driver.find_elements_by_tag_name("a")[0]
        header = self.driver.find_element(By.TAG_NAME, 'h1').text
        self.assertIn("JUST AN ART", header)

    def test_home_page_blog(self):
        #под шапкой расположен блог со статьями
        self.driver.get("http://127.0.0.1:8000/")
        content_container = self.driver.find_elements(By.CLASS_NAME, "col-md-8")
        self.assertTrue(content_container)

    def test_home_page_blog_post_looks_correct(self):
        #у каждой статьи есть заголовок и один абзац с текстом
        self.driver.get("http://127.0.0.1:8000/")
        blog_post_title = self.driver.find_elements(By.TAG_NAME,'h1')
        blog_post_text = self.driver.find_elements(By.TAG_NAME,'P')
        self.assertTrue(blog_post_title)
        self.assertTrue(blog_post_text)



if __name__ == "__main__":
    unittest.main()




