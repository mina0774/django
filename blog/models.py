from django.conf import settings
from django.db import models
from django.utils import timezone

class Menu(models.Model):
    parent_title_choices=(('Profile','Profile'),('Activity','Activity'),('Project','Project'))
    parent_title=models.CharField(max_length=30,choices=parent_title_choices,default='Profile')
    index_title_choices=(('Profile',(('Skill','Skill'),)),('Activity',(('UCI Undergraduate Researcher','UCI Undergraduate Researcher'),('Coding HelpDesk','Coding HelpDesk'),('Heronation InternShip','Heronation InternShip'))),('Project',(('Face Recogntion','Face Recognition'),('Mu:Ping App','Mu:Ping App'),('Ang-Bob App','Ang-Bob App'),('Flex-Bison Interpreter','Flex-Bison Interpreter'),('Z-shop App','Z-shop App'),)))
    index_title=models.CharField(max_length=30,choices=index_title_choices,default='Skill')

    def __str__(self):
        return self.index_title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    menu=models.ForeignKey('blog.Menu',on_delete=models.CASCADE,related_name='posts')
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

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    post=models.ForeignKey('blog.Post',on_delete=models.CASCADE,related_name='comments') # related_name은 post 모델에서 댓글에 접근할 수 있게 함. ex> post.comments.all()
    author=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)
    groupno=models.IntegerField(default=0)
    orderno=models.IntegerField(default=0)
    depth=models.IntegerField(default=0)

    def approve(self):
        self.approved_comment=True
        self.save()

    def __str__(self):
        return self.text
