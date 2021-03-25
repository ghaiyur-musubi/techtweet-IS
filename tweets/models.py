from django.db import models

"""
tweet_user - CharField

"""

class tweet_db(models.Model):
    class Meta(object):
        db_table = 'tweets'

    tweet_user = models.CharField(
        'Twitter User Name', blank=False, null=False, max_length=20, db_index=True, default='Anonymous')

    

    

    


