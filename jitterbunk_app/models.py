from django.db import models


class User(models.Model):
    """
    Users can Bunk other usersls

    user: name of the user
    photo: name of image within static folder
    """
    user = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user


class Bunk(models.Model):
    """
    Bunks are poke-like objects, viewed on the main feed

    from_user: user that committed the Bunk
    to_user: user that got bunked
    time: time of the bunk
    """
    from_user = models.ForeignKey(User,
                                  related_name='from_user')
    to_user = models.ForeignKey(User,
                                related_name='to_user')
    time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "from " + str(self.from_user) + ", to " + str(self.to_user)
