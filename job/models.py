from django.db import models
from profiles.models import Profile
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

JOBSTATUS_CHOICES = (
    ('Job', 'Job'),
    ('Contract', 'Contract'),
    ('Internship', 'Internship'),
    ('Part-Time', 'Part-Time'),
)

class Job(models.Model):
    company_name = models.CharField(max_length = 15000)
    job_title = models.CharField(max_length = 600)
    education = models.CharField(max_length = 17000, default='', null = True, blank = True)
    company_logo = models.ImageField(upload_to = 'upload/company_profile/')
    experience = models.IntegerField()
    industry = models.CharField(max_length = 120000, default='', null = True, blank = True)
    company_description = RichTextField()
    job_details = RichTextField()
    location = models.CharField(max_length = 12000, default='', null = True, blank = True)
    recruiter = models.CharField(max_length = 4500, default='', null = True, blank = True)
    contact = models.CharField(max_length = 12000, default = '', null = True, blank = True)
    payrate = models.CharField(max_length = 1500, default='', null = True, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    skills_tag = TaggableManager()
    job_status = models.CharField(max_length = 150, choices = JOBSTATUS_CHOICES)
    apply_by = models.DateField()
    Duration = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return self.company_name 

    def get_status(self):
        return self.dashboard_set.all()

JOB_STATUS = (
    ('Applied', 'Applied'),
    ('Seen', 'Seen'),
    ('Not-Selected', 'Not-Selected'),
    ('In-Touch', 'In-Touch')
)

class Dashboard(models.Model):
    job = models.ForeignKey(Job, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    resume = models.FileField(upload_to ='uploads/resume/')
    email = models.EmailField()
    phone = models.CharField(max_length = 20)
    job_status = models.CharField(max_length = 100, choices = JOB_STATUS)
    date_applied = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email

    def job_applied(self):
        return self.job.count()