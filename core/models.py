from django.db import models


class Project(models.Model):
    name = models.CharField('Project name', max_length=100)
    description = models.TextField('Project description', null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Company{{{}}}".format(self.name)


class Release(models.Model):

    RELEASE_STATUS = (
        ('SUCCESS', 'Success'),
        ('ERROR', 'Error'),
        ('DEPLOYING', 'deploying'),
    )

    date = models.DateTimeField('Release date', auto_now=True)
    commit_id = models.CharField('Commit id', max_length=64, null=True)
    commit_description = models.TextField('Commit description', null=True)
    description = models.TextField('Release description', null=True)
    status = models.CharField('Release status', max_length=20, choices=RELEASE_STATUS)
    project = models.ForeignKey('Project', Project)

    def __str__(self):
        return self.commit_id

    def __repr__(self):
        return "Release{{{}: {}}}".format(self.commit_id, self.commit_description)