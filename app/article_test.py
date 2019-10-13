import unittest
from Models import article
Article = article.Article


class ArticleTest(unittest.TestCase):

    '''
      Test Class to test the behaviour of the   article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('fake-title','marion','https://s.image.com','2019-10-12T03:11:28Z',"http://abc.com",'abc-news')

    def test_article_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
    unittest.main()