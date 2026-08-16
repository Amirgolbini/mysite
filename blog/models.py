from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    city = models.CharField(max_length=100, default='گرگان')
    price_per_night = models.BigIntegerField(default=1200000)
    bedrooms = models.IntegerField(default=2)
    bathrooms = models.IntegerField(default=1)
    capacity_base = models.IntegerField(default=4)
    capacity_max = models.IntegerField(default=6)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Reservation(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reservations', verbose_name='اقامتگاه')
    full_name = models.CharField(max_length=150, verbose_name='نام و نام خانوادگی')
    phone_number = models.CharField(max_length=20, verbose_name='شماره تلفن')
    check_in = models.DateField(verbose_name='تاریخ ورود')
    check_out = models.DateField(verbose_name='تاریخ خروج')
    total_price = models.BigIntegerField(default=0, verbose_name='مبلغ کل (تومان)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    class Meta:
        verbose_name = 'رزرو'
        verbose_name_plural = 'رزروها'

    def __str__(self):
        return f"{self.full_name} - {self.post.title} ({self.check_in} تا {self.check_out})"