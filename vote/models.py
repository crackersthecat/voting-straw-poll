from django.db import models


class Constituency(models.Model):
    constituency_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.constituency_name

    def get_constituencies():
        return Constituency.objects.all()


class Party(models.Model):
    party_name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.party_name


class Response(models.Model):
    will_you_vote = models.BooleanField(default=True)
    constituency = models.ForeignKey(Constituency, null=True)
    party = models.ForeignKey(Party, null=True)

    def __unicode__(self):
        return 'Response ' + str(self.id)

    @classmethod
    def create(cls, will_you_vote, constituency, party):
        response = cls(will_you_vote=will_you_vote, constituency=constituency, party=party)
        # do something with the book
        return response
