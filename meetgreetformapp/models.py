from django.db import models




class Fans(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()
    occupation = models.CharField(max_length=100)
    age = models.IntegerField()
    civil_status = models.CharField(max_length=50)
    citizenship = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    religion = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    will_you_have_a_guest_with_you = models.CharField(max_length=50)
    would_you_like_to_be_updated_about_the_upcoming_tour = models.CharField(max_length=50)
    how_long_have_you_been_supporting_leeminho = models.CharField(max_length=50)
    do_you_have_his_membership_card = models.CharField(max_length=50)
    which_category_of_fan_card_do_you_have = models.CharField(max_length=50)
    do_you_have_ticket_for_minhoverse = models.CharField(max_length=50, default=None)
    if_yes_which_of_the_ticket_category_and_country_do_you_have = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name





