from django.db import models
from django.urls import reverse
# Create your models here.


from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    language = models.CharField(max_length=2)
    


class Post(models.Model):

    Csharp = 'C#'
    Cplus = 'C++'
    Python = 'Python'
    JavaScript = 'JavaScript'
    Java = 'Java'
    HTML = 'HTML'
    CSS  = 'CSS'
    SQL  = 'SQL'
    C   = 'C'
    TypeScript = 'TypeScript'
    PHP = 'PHP'
    R  = 'R'
    BashShell = 'Bash/Shell'
    Go = 'Go'
    Swift = 'Swift'
    all = 'all'
    
    CHOICES_IN_LANGUAGES = [

         ('Python',Python),
         ('JavaScript',JavaScript),
         ('Java',Java),
         ('HTML',HTML),
         ('CSS',CSS),
         ('SQL',SQL),
         ('C#',Csharp),
         ('C',C),
         ('C++',Cplus),
         ('TypeScript',TypeScript),
         ('PHP',PHP),
         ('R',R),
         ('Bash/Shell',BashShell),
         ('Go',Go),
         ('Swift',Swift),
         ('all',all)
    ]

    name = models.CharField(max_length=25)
    company_name = models.CharField(max_length=20)

    what_we_do = models.TextField()
    requirement = models.TextField(blank=False,null=False)

    main_language = models.CharField(max_length=15,choices=CHOICES_IN_LANGUAGES,default=all) #THIS DETERMINE MAIN LANGUAGE 

    experienced = [('0',0),("1",1),("2",2),("3",3),("4",4),("5",5)]
    experience = models.CharField(max_length=1,choices=experienced) # THIS IS DETERMINE EXPERIENCE LEVEL 

    base_salary = models.PositiveIntegerField(null = False,blank=False)
    tgUsername = models.CharField(max_length=15,blank=False,null=False)

    #created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('url',args = [str(self.id)])

    def __str__(self) -> str:
        return self.company_name

class Jobs(models.Model):

     name = models.CharField(max_length=20)
     comacompany_name = models.CharField(max_length=20)
     experienced = [('0',0),("1",1),("2",2),("3",3),("4",4),("5",5)]
     experience = models.CharField(max_length=1,choices=experienced)
     tgUsername = models.CharField(max_length=15,blank=False,null=False)
     created_at = models.DateTimeField(auto_now_add=True)


     def get_absolute_url(self):
         return reverse ('url',args = [str(self.id)])

     def __str__(self) -> str:
         return self.comacompany_name
