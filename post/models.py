from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# class VotesManager(models.Manager):
#     def add_count(self, user, post):
#         obj, created = self.model.objects.get_or_create(
#             user=user,
#             post=post
#         )
#         obj.count = obj.count_upvotes.count()
#         obj.save()
#         return obj


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    upvotes = models.ManyToManyField(User, related_name="votes", blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-creation_date']
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def total_votes(self):
        return self.upvotes.count()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'id': self.id})


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
