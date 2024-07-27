from django.db import models


class TimestampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Categories(TimestampedModel):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Lesson(TimestampedModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    description = models.TextField(max_length=150)
    price_per_month = models.SmallIntegerField(default=0)
    lessons_count = models.SmallIntegerField(default=0)
    lessons_duration = models.CharField(max_length=10)
    pupils_count = models.SmallIntegerField(default=0)
    team_lead = models.BooleanField(default=False)
    team_lead_name = models.CharField(max_length=30)
    company_address = models.CharField(max_length=50)
    support_phone_number = models.CharField(max_length=9)
    start_date = models.DateField()
    slug = models.SlugField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title

