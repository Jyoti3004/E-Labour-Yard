from django.db import models

# Create your models here.
GENDER_CHOICES = (('Male','Male'),('Female','Female'),('Others','others'))
WORK_CHOICES = [
    ('1','Plumber'),
    ('2','Carpenter'),
    ('3','Painter'),
    ('4','Electrician'),
    ('5','Roofer'),
    ('6','others')
]
class register1(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=30)
    address=models.TextField()
    type_of_user=models.CharField(max_length=25)

    def __str__(self):
        return self.name
# class ADMIN(models.Model):
#     A_PSWD = models.CharField(max_length=10)
#     A_NAME = models.CharField(max_length=25)
#     A_Phone_No = models.BigIntegerField()
#     A_EMAIL_ID = models.EmailField()
#     GENDER = models.CharField(choices=GENDER_CHOICES,max_length=20)
#
# class CONTRACTOR(models.Model):
#     C_PSWD =models.CharField(max_length=10)
#     C_NAME = models.CharField(max_length=25)
#     C_Phone_No = models.BigIntegerField()
#     C_EMAIL_ID = models.EmailField()
#
# class END_USER(models.Model):
#     E_NAME = models.CharField(max_length=25)
#     E_Phone_No = models.BigIntegerField()
#     E_EMAIL_ID = models.EmailField()
#     E_ADDRESS = models.TextField()
#
# class LABOUR(models.Model):
#     L_PSWD = models.CharField(max_length=10)
#     L_NAME = models.CharField(max_length=25)
#     L_Phone_No = models.BigIntegerField()
#     L_EMAIL_ID = models.EmailField()
#     GENDER = models.CharField(choices=GENDER_CHOICES, max_length=20)
#     TYPE_OF_WORK =models.CharField(choices=WORK_CHOICES,max_length=15)
#
# class WORK(models.Model):
#     L_ID=models.ForeignKey(LABOUR,on_delete=models.CASCADE)
#     TYPE_OF_WORK = models.CharField(choices=WORK_CHOICES,max_length=15)
#
# class FEEDBACK(models.Model):
#     C_ID=models.ForeignKey(CONTRACTOR,on_delete=models.CASCADE)
#     E_ID=models.ForeignKey(END_USER,on_delete=models.CASCADE)
#     L_ID = models.ForeignKey(LABOUR, on_delete=models.CASCADE)
#     COMMENT=models.TextField()
#     RATING=models.IntegerField()
#
# class REQUEST(models.Model):
#     E_ID = models.ForeignKey(END_USER, on_delete=models.CASCADE)
#     C_ID = models.ForeignKey(CONTRACTOR, on_delete=models.CASCADE)
#     R_DATE=models.DateTimeFsield()
#     TYPE_OF_WORK = models.CharField(choices=WORK_CHOICES,max_length=15)
#     NO_OF_LABOUR=models.IntegerField()
#     R_STATUS=models.CharField(max_length=15)
#     REQUEST_DESC=models.TextField()
#
class profile1(models.Model):
    name = models.CharField(max_length=30)
    userid = models.ForeignKey(register1,on_delete=models.CASCADE,null=True)
    phone = models.BigIntegerField()
    email = models.EmailField()
    exp = models.IntegerField()
    address = models.TextField()
    des = models.TextField()
    img = models.ImageField(upload_to="photos")

class work1(models.Model):
    userid = models.ForeignKey(register1, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=25)
    phone = models.IntegerField(null=True)
    location = models.CharField(max_length=25)
    types_of_labour = models.CharField(max_length=25)
    no_of_labour = models.IntegerField()
    exp = models.IntegerField(null=True)
    Working_Hour = models.CharField(max_length=25,null=True)
    income_per_day = models.BigIntegerField()
    img = models.ImageField(upload_to="photos",null=True)
    message = models.TextField()
    def __str__(self):
        return self.name


class endwork1(models.Model):
    userid = models.ForeignKey(register1, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=25)
    phone = models.IntegerField(null=True)
    location = models.CharField(max_length=25)
    types_of_labour = models.CharField(max_length=25)
    no_of_labour = models.IntegerField()
    exp = models.IntegerField(null=True)
    Working_Hour = models.CharField(max_length=25, null=True)
    income_per_day = models.BigIntegerField()
    img = models.ImageField(upload_to="photos", null=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class requestsdata(models.Model):
    workid = models.ForeignKey(work1,on_delete=models.CASCADE)
    labourid = models.ForeignKey(register1,on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

class requestsdataforenduser(models.Model):
    workid = models.ForeignKey(endwork1,on_delete=models.CASCADE)
    labourid = models.ForeignKey(register1,on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)


class contact1(models.Model):
   name = models.CharField(max_length=30)
   email = models.EmailField()
   subject = models.CharField(max_length=30)
   message = models.CharField(max_length=50)


class LFEEDBACK(models.Model):
    Labour_name=models.CharField(max_length=20)
    C_ID = models.ForeignKey(register1, on_delete=models.CASCADE)
    COMMENT=models.TextField()
    RATING=models.IntegerField()

# class EFEEDBACK(models.Model):
#     enduser_name=models.CharField(max_length=20)
#     L_ID = models.ForeignKey(register1, on_delete=models.CASCADE)
#     COMMENT=models.TextField()
#     RATING=models.IntegerField()









