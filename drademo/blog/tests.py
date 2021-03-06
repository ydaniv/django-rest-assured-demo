import datetime
from rest_assured.testcases import ReadWriteRESTAPITestCaseMixin, BaseRESTAPITestCase
from . import factories


class EntryAPITestCase(ReadWriteRESTAPITestCaseMixin, BaseRESTAPITestCase):

    base_name = 'entry' # this is the base_name generated by the DefaultRouter
    factory_class = factories.Entry
    user_factory = factories.User
    update_data = {'rating': 5}

    def setUp(self):
       self.author = factories.Author.create()
       super(EntryAPITestCase, self).setUp()

    def get_object(self, factory):
        return factory.create(authors=[self.author])

    def get_create_data(self):
       return {'headline': 'Lucifer Sam',
               'body_text': 'is a song by British psychedelic rock band Pink Floyd.',
               'authors': [self.author.pk],
               'rating': 4,
               'n_pingbacks': 0,
               'n_comments': 0,
               'pub_date': datetime.date(2014, 11, 12),
               'blog': self.object.blog.pk}
