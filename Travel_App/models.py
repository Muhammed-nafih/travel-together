from django.db import models

# Create your models here.


class userDetails(models.Model):
	Name = models.CharField(max_length=100,default=None,null=True)
	Age = models.CharField(max_length=100,default=None,null=True)
	Address = models.CharField(max_length=100,default=None,null=True)
	Phone = models.CharField(max_length=100,default=None,null=True)
	Email = models.CharField(max_length=100,default=None,null=True)
	Image = models.ImageField(upload_to="images/",null=True)
	Username = models.CharField(max_length=100,default=None,null=True)
	Password = models.CharField(max_length=100,default=None,null=True)
	class Meta:
		db_table = 'userDetails'

class Groups(models.Model):
	user_id = models.CharField(max_length=100,default=None,null=True)
	Name = models.CharField(max_length=100,default=None,null=True)
	Description = models.CharField(max_length=100,default=None,null=True)
	Status = models.CharField(max_length=100,default=None,null=True)
	Image = models.ImageField(upload_to="GroupImages/",null=True)
	class Meta:
		db_table = 'Groups'

class JoinRequest(models.Model):
    user = models.ForeignKey(userDetails, on_delete=models.CASCADE,null=True)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=100, default='Pending',null=True)
    requested_at = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        db_table = 'JoinRequests'



class Member(models.Model):
    user = models.ForeignKey(userDetails, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Member'


class Chat(models.Model):
	user = models.ForeignKey(userDetails, on_delete=models.CASCADE,null=True)
	group = models.ForeignKey(Groups, on_delete=models.CASCADE,null=True)
	comment = models.CharField(max_length=200,default=None,null=True)
	class Meta:
		db_table = "Chat"


 