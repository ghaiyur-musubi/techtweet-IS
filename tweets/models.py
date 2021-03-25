from django.db import models

"""
user - CharField
"""

class tweet_db(models.Model):
    class Meta(object):
        db_table = 'tweets'

    


