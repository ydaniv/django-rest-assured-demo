import datetime
import factory
from factory import fuzzy
from django.contrib import auth
from . import models


class Blog(factory.DjangoModelFactory):

    class Meta:
        model = models.Blog

    name = factory.Sequence(lambda n: 'Blog {0}'.format(n))
    tagline = factory.Sequence(lambda n: 'Blog {0} tag line'.format(n))


class Author(factory.DjangoModelFactory):

    class Meta:
        model = models.Author

    name = factory.Sequence(lambda n: 'Author {0}'.format(n))
    email = factory.Sequence(lambda n: 'author{0}@example.com'.format(n))


class Entry(factory.DjangoModelFactory):

    class Meta:
        model = models.Entry

    blog = factory.SubFactory(Blog)
    headline = factory.Sequence(lambda n: 'OMG Headline {0}!'.format(n))
    body_text = fuzzy.FuzzyText(length=100)
    pub_date = datetime.date(2014, 11, 12)
    mod_date = datetime.date(2014, 11, 12)
    rating = fuzzy.FuzzyInteger(low=1, high=5, step=1)
    n_pingbacks = 0
    n_comments = 0

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for author in extracted:
                self.authors.add(author)


class User(factory.DjangoModelFactory):

    class Meta:

        model = auth.get_user_model()
        exclude = ('raw_password',)

    first_name = 'Robert'
    last_name = factory.Sequence(lambda n: 'Paulson the {0}'.format(n))
    email = factory.sequence(lambda n: 'account{0}@example.com'.format(n))
    username = 'mayhem'
    raw_password = '123'
    password = factory.PostGenerationMethodCall('set_password', raw_password)
    is_active = True
