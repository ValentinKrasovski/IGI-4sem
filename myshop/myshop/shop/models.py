from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.utils import timezone


# Модели для Главной страницы
class Article(models.Model):
    title = models.CharField(max_length=200)
    short_content = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Advertisement(models.Model):
    adv_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='advertisement')
    link = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('advertisement-detail', args=[str(self.id)])

    def str(self):
        return self.adv_name

class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/')
    website = models.URLField()

    def __str__(self):
        return self.name


# О компании
class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/')
    description = models.TextField()
    video_url = models.URLField()
    year_founded = models.PositiveIntegerField()
    history = models.TextField()
    requisites = models.TextField()


# Частозадаваемые вопросы
class FAQ(models.Model):
    user_name = models.CharField(max_length=255, verbose_name='Имя пользователя')
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.question


# Контакты
class Employee(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    image = models.ImageField(upload_to='contacts/')
    position = models.CharField(max_length=100, verbose_name='Должность')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# Политика
class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


# Вакансии
class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    application_deadline = models.DateField()

    def __str__(self):
        return self.title


# Отзывы
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} - {self.date_added}"

class ActiveCouponManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True, valid_to__gte=timezone.now())

# Промокоды
class Coupon(models.Model):
    code = models.CharField(max_length=15, unique=True)
    description = models.TextField(blank=True, null=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    objects = models.Manager()  # Менеджер по умолчанию
    active_coupons = ActiveCouponManager()  # Кастомный менеджер для активных купонов

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if self.valid_to < timezone.now() and self.active:
            self.active = False
        super(Coupon, self).save(*args, **kwargs)
#     def __str__(self):
#         return self.code
#
#
# @receiver(post_save, sender=Coupon)
# def set_coupon_active(sender, instance, **kwargs):
#     if instance.valid_to < timezone.now() and instance.active:
#         instance.active = False
#         instance.save()


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]
        # index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class Client(models.Model):
    first_name = models.CharField(max_length=200,
                                  help_text='Enter first name')
    last_name = models.CharField(max_length=200,
                                 help_text='Enter last name')
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=50,
                                    help_text='Enter phone number')

    def get_absolute_url(self):
        return reverse('client-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)
