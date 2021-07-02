from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField( max_length=150)
    verify = models.BooleanField(default=False)


# class Location(model.Model):
#     st=(
#     ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
#     ('Andra Pradesh ','Andra Pradesh '),
#     ('Arunachal Pradesh ','Arunachal Pradesh '),
#     ('Assam ','Assam '),
#     ('Bihar ','Bihar' ),
#     ('Chandigarh ','Chandigarh'),
#     ('Chattisgarh ','Chattisgarh'),
#     ('Dadra & Nagar Haveli ','Dadra & Nagar Haveli'),
#     ('Daman & Diu ','Daman & Diu'),
#     ('Delhi  ','Delhi '),
#     ('Gujarat ','Gujarat'),
#     ('Haryana ','Haryana'),
#     ('Himachal Pradesh ','Himachal Pradesh'),
#     ('Jammu & Kashmir ','Jammu & Kashmir'),
#     ('Jharkhand ','Jharkhand'),
#     ('Karnataka ','Karnataka'),
#     ('Kerala ','Kerala'),
#     ('Lakshadweep ','Lakshadweep'),
#     ('Madhya Pradesh ','Madhya Pradesh'),
#     ('Maharastra ','Maharastra'),
#     ('Manipur ','Manipur'),
#     ('Meghalaya ','Meghalaya'),
#     ('Mizoram ','Mizoram'),
#     ('Nagaland ','Nagaland'),
#     ('Odisha ','Odisha'),
#     ('Puducherry ','Puducherry'),
#     ('Punjab ','Punjab'),
#     ('Rajasthan ','Rajasthan'),
#     ('Sikkim ','Sikkim'),
#     ('Tamil Nadu ','Tamil Nadu'),
#     ('Telangana ','Telangana'),
#     ('Tripura ','Tripura'),
#     ('Uttarakhand ','Uttarakhand'),
#     ('Utter Pradesh ','Utter Pradesh'),
#     ('West Bengal ','Wesh Bengal'),

# )
#     state = models.CharField(choices=st, max_length=50)

#                                                                                                                      24,5           3%
