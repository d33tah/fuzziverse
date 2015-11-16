from django.db import models
import uuid

class Application(models.Model):
    name = models.CharField(max_length=1024)
    url = models.CharField(max_length=1024)

class Report(models.Model):
    title = models.CharField(max_length=1024)
    url = models.CharField(max_length=1024)
    app = models.ForeignKey(Application)

class FuzzingAttempt(models.Model):
    app = models.ForeignKey(Application)
    fuzzer_stats = models.TextField(verbose_name='fuzzer_stats contents')

def upload_path_handler(instance, filename):
    return 'static/%s' % uuid.uuid4()

class InputTestCase(models.Model):
    the_file = models.FileField(upload_to=upload_path_handler)
    attempt = models.ForeignKey(FuzzingAttempt)
