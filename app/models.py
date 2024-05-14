from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager,AbstractUser
# Create your models here.
class User(AbstractUser):
    username = models.CharField(unique=True,null=True,max_length=100)
    email = models.EmailField(unique=True,null=True)
    orgbox = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(upload_to='profile-images/', null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    sem_1 = models.DateTimeField(blank=True, null=True)
    sem_2 = models.DateTimeField(blank=True, null=True)
    YEAR_SECTION_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
    ]
    
    year_section = models.CharField(max_length=10, choices=YEAR_SECTION_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    USERNAME_FIELDS = 'username'
    REQUIRED_FIELDS = []

#homepage
    
class Banner(models.Model):
    sub_text = models.CharField(max_length=100,blank=True)
    primary_text = models.CharField(max_length=100,blank=True)
    primary_sub = models.CharField(max_length=100,blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.primary_text
    
class AboutPic(models.Model):
    image = models.ImageField(upload_to='about-pic-upload/')
    image_title = models.CharField(max_length=50,blank=True)
    description = models.TextField()
    
    def __str__(self):
        return self.image_title
    
class HighlightsEvent(models.Model):
    url = models.URLField(max_length=255, blank=True)
    image = models.ImageField(upload_to='highlights-event/')
    title = models.CharField(max_length=200, blank=True)
    time = models.TimeField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True, verbose_name="Start ng date")
    date_from = models.DateField(blank=True, null=True, verbose_name="End ng date")
    location = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True, null=True)
    link_desc = models.CharField(max_length=255, blank=True)
    details = models.CharField(max_length=100, blank=True, verbose_name="Hosted By")
    learn_more = models.URLField(max_length=255,blank=True)
    
    def __str__(self):
        return self.title
    
class SoftwareTools(models.Model):
    url = models.URLField(max_length=255, blank=True)
    image = models.ImageField(upload_to='software-tools/')
    
class SoftwareToolsResource(models.Model):
    url = models.URLField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length = 255, blank=True, null=True)
    image = models.ImageField(upload_to='software-resources/')
    desc = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return self.title
    
class Payment(models.Model):
    acct_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='payment-qr/')
    
    def __str__(self):
        return self.email
    
class OfficerYear(models.Model):
    YEAR_CHOICES = [
        ('2020-2021', '2020-2021'),
        ('2021-2022', '2021-2022'),
        ('2022-2023', '2022-2023'),
        ('2023-2024', '2023-2024'),
        ('2024-2025', '2024-2025'),
        ('2025-2026', '2025-2026'),
        ('2026-2027', '2026-2027'),
        ('2027-2028', '2027-2028'),
        ('2028-2029', '2028-2029'),
        ('2029-2030', '2029-2030'),
        ('2030-2031', '2030-2031'),
        ('2031-2032', '2031-2032'),
        ('2032-2033', '2032-2033'),
        ('2033-2034', '2033-2034'),
        ('2034-2035', '2034-2035'),
        ('2035-2036', '2035-2036'),
        ('2036-2037', '2036-2037'),
        ('2037-2038', '2037-2038'),
        ('2038-2039', '2038-2039'),
        ('2039-2040', '2039-2040'),
        ('2040-2041', '2040-2041'),
        ('2041-2042', '2041-2042'),
        ('2042-2043', '2042-2043'),
        ('2043-2044', '2043-2044'),
        ('2044-2045', '2044-2045'),
        ('2045-2046', '2045-2046'),
        ('2046-2047', '2046-2047'),
        ('2047-2048', '2047-2048'),
        ('2048-2049', '2048-2049'),
        ('2049-2050', '2049-2050')
    ]

    
    year = models.CharField(choices=YEAR_CHOICES, blank=True, null=True, max_length=255)

    def __str__(self):
        return str(self.year)
    
class AboutUsContext(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='abous_us_context/', blank=True, null=True)
    
class VisionMissionGoal(models.Model):
    vision = models.CharField(max_length=255, blank=True, null=True)
    mission = models.CharField(max_length=255, blank=True, null=True)
    goal = models.CharField(max_length=255, blank=True, null=True)

class ExecutiveBanner(models.Model):
    year = models.ForeignKey(OfficerYear, models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='executive_banner/', blank=True)

class ExecutiveOfficer(models.Model):
    year = models.ForeignKey(OfficerYear, models.SET_NULL, blank=True, null=True)
    president = models.CharField(max_length=100, blank=True)
    president_img = models.ImageField(upload_to='president', blank=True)
    vp_internal = models.CharField(max_length=100, blank=True)
    vp_internal_img = models.ImageField(upload_to='vp_internal', blank=True)
    vp_external = models.CharField(max_length=100, blank=True)
    vp_external_img = models.ImageField(upload_to='vp_external', blank=True)
    secretary = models.CharField(max_length=100, blank=True)
    secretary_img = models.ImageField(upload_to='secretary', blank=True)
    assistant_secretary = models.CharField(max_length=100, blank=True)
    assistant_secretary_img = models.ImageField(upload_to='assistant_secretary', blank=True)
    treasurer = models.CharField(max_length=100, blank=True)
    treasurer_img = models.ImageField(upload_to='treasurer', blank=True)
    assistant_treasurer = models.CharField(max_length=100, blank=True)
    assistant_treasurer_img = models.ImageField(upload_to='assistant_treasurer', blank=True)
    auditor = models.CharField(max_length=100, blank=True)
    auditor_img = models.ImageField(upload_to='auditor', blank=True)
    pro = models.CharField(max_length=100, blank=True)
    pro_img = models.ImageField(upload_to='pro', blank=True)
    
    
class MultimediaAssistant(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='multimedia_assistant/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class MultimediaTeam(models.Model):
    year = models.ForeignKey(OfficerYear, models.SET_NULL, blank=True, null=True)
    multimedia_head = models.CharField(max_length=100, blank=True, null=True)
    multimedia_head_img = models.ImageField(upload_to='multimedia_head/', blank=True, null=True)
    assistants = models.ManyToManyField(MultimediaAssistant)

    def __str__(self):
        return self.multimedia_head
    
class ProgrammingAssistant(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='programming_assistant/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class ProgrammingTeam(models.Model):
    year = models.ForeignKey(OfficerYear, models.SET_NULL, blank=True, null=True)
    programming_head = models.CharField(max_length=100, blank=True, null=True)
    programming_head_img = models.ImageField(upload_to='programming_head/', blank=True, null=True)
    assistants = models.ManyToManyField(ProgrammingAssistant)

    def __str__(self):
        return self.programming_head
    
class WritersAssistant(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='writers_assistant/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class WritersTeam(models.Model):
    year = models.ForeignKey(OfficerYear, models.SET_NULL, blank=True, null=True)
    writers_head = models.CharField(max_length=100, blank=True, null=True)
    writers_head_img = models.ImageField(upload_to='writers_head/', blank=True, null=True)
    assistants = models.ManyToManyField(WritersAssistant)

    def __str__(self):
        return self.writers_head

class EsportsAssistant(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='esports_assistant/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class EsportsTeam(models.Model):
    year = models.ForeignKey(OfficerYear, models.SET_NULL, blank=True, null=True)
    esports_head = models.CharField(max_length=100, blank=True, null=True)
    esports_head_img = models.ImageField(upload_to='esports_head/', blank=True, null=True)
    assistants = models.ManyToManyField(EsportsAssistant)

    def __str__(self):
        return self.esport_head

class DocumentationAssistant(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='documentation_assistant/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class DocumentationTeam(models.Model):
    year = models.ForeignKey(OfficerYear, models.SET_NULL, blank=True, null=True)
    documentation_head = models.CharField(max_length=100, blank=True, null=True)
    documentation_head_img = models.ImageField(upload_to='documentation_head/', blank=True, null=True)
    assistants = models.ManyToManyField(DocumentationAssistant)

    def __str__(self):
        return self.documentation_head
    
    
class SocialMediaAssistant(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='social_media_assistant/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class SocialMediaTeam(models.Model):
    year = models.ForeignKey(OfficerYear, models.SET_NULL, blank=True, null=True)
    social_media_head = models.CharField(max_length=100, blank=True, null=True)
    social_media_head_img = models.ImageField(upload_to='social_media_head/', blank=True, null=True)
    assistants = models.ManyToManyField(SocialMediaAssistant)

    def __str__(self):
        return self.social_media_head