from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent_title_choices=(('Profile','Profile'),('Activity','Activity'),('Project','Project'))
    parent_title=models.CharField(max_length=30,choices=parent_title_choices,default='Profile')
    index_title_choices=(('Profile',(('Skill','Skill'),)),('Activity',(('UCI Undergraduate Researcher','UCI Undergraduate Researcher'),('Coding HelpDesk','Coding HelpDesk'),('Heronation InternShip','Heronation InternShip'))),('Project',(('Face Recogntion','Face Recognition'),('Mu:Ping App','Mu:Ping App'),('Ang-Bob App','Ang-Bob App'),('Flex-Bison Interpreter','Flex-Bison Interpreter'),('Z-shop App','Z-shop App'),)))
    index_title=models.CharField(max_length=30,choices=index_title_choices,default='Skill')
    title = models.CharField(max_length=200)
    period=models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
