from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان اقامتگاه")
    content = models.TextField(verbose_name="توضیحات اقامتگاه")
    status = models.BooleanField(default=True, verbose_name="وضعیت انتشار")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    counted_views = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    # فیلدهای اقامتگاه
    price_per_night = models.PositiveIntegerField(default=0, verbose_name="قیمت هر شب (تومان)")
    city = models.CharField(max_length=100, default="نامشخص", verbose_name="شهر")
    bedrooms = models.PositiveSmallIntegerField(default=1, verbose_name="تعداد اتاق خواب")
    bathrooms = models.PositiveSmallIntegerField(default=1, verbose_name="تعداد سرویس بهداشتی")
    capacity_base = models.PositiveSmallIntegerField(default=2, verbose_name="ظرفیت پایه (نفر)")
    capacity_max = models.PositiveSmallIntegerField(default=4, verbose_name="حداکثر ظرفیت (نفر)")

    def __str__(self):
        return self.title


class Reservation(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reservations', verbose_name="اقامتگاه")
    full_name = models.CharField(max_length=150, verbose_name="نام و نام خانوادگی")
    phone_number = models.CharField(max_length=15, verbose_name="شماره تلفن")
    check_in = models.DateField(verbose_name="تاریخ ورود")
    check_out = models.DateField(verbose_name="تاریخ خروج")
    total_price = models.PositiveIntegerField(default=0, verbose_name="قیمت کل (تومان)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    class Meta:
        verbose_name = "رزرو"
        verbose_name_plural = "رزروها"



    def __str__(self):
        return f"رزرو {self.post.title} توسط {self.full_name} ({self.phone_number})"