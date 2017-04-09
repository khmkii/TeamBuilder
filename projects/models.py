from django.core.urlresolvers import reverse
from django.db import models


class Profile(models.Model):

    story = models.TextField(default='')
    avatar = models.FileField(null=True, upload_to='user_avatars/', blank=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    middle_name = models.CharField(null=True, blank=True, max_length=50, default='')
    user = models.OneToOneField('accounts.SiteUser', on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    skills = models.ManyToManyField('projects.Skill')

    def __str__(self):
        return f'{self.user.username} profile'

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={'slug': self.slug})


class Skill(models.Model):

    ANDROID_DEV = 1
    DES = 2
    JAVA_DEV = 3
    PHP_DEV = 4
    PYTHON_DEV = 5
    RAILS_DEV = 6
    WORDPRESS_DEV = 7
    IOS_DEV = 8

    SKILLS = (
        (str(ANDROID_DEV), 'Android Developer'),
        (str(DES), 'Designer'),
        (str(JAVA_DEV), 'Java Developer'),
        (str(PHP_DEV), 'PHP Developer'),
        (str(PYTHON_DEV), 'Python Developer'),
        (str(RAILS_DEV), 'Rails Developer'),
        (str(WORDPRESS_DEV), 'WordPress Developer'),
        (str(IOS_DEV), 'iOS Developer'),
    )

    name = models.CharField(
        choices=SKILLS,
        max_length=1,
        default='',
    )

    def __str__(self):
        return self.get_name_display()


class Project(models.Model):
    title = models.CharField(max_length=150, default='')
    description = models.TextField(default='')
    owner = models.OneToOneField('accounts.SiteUser', null=True)
    recruited = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)


class Position(models.Model):
    project = models.ForeignKey('projects.Project')
    expertise = models.OneToOneField('projects.Skill')


class Application(models.Model):
    applicant = models.OneToOneField('accounts.SiteUser', null=True)
    success = models.BooleanField(default=False)
    position = models.OneToOneField('projects.Position', null=True)
