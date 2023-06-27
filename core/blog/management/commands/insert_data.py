from django.core.management.base import BaseCommand

from faker import Faker
from datetime import datetime
import random

from accounts.models import User, Profile
from blog.models import Post, Category


category_list = ['it','iot','design']



class Command(BaseCommand):
    help = "Closes the specified poll for voting"


    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()



    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(), password="test@123456")
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()


        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(10):
            Post.objects.create(
            author = profile,
            title = self.fake.paragraph(nb_sentences=1),
            content = self.fake.paragraph(nb_sentences=10),
            status = True,
            category = Category.objects.get(name = random.choice(category_list)),
            published_date = datetime.now()
        )