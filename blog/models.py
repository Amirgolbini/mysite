from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    #image
    #author
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tag
    #category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)
    capacity_max = models.PositiveSmallIntegerField(default=4, verbose_name="حداکثر ظرفیت (نفر)")
    title = models.CharField(max_length=200, verbose_name="عنوان اقامتگاه")
    content = models.TextField(verbose_name="توضیحات اقامتگاه")
    status = models.BooleanField(default=True, verbose_name="وضعیت انتشار")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    counted_views = models.IntegerField(default=0, verbose_name="تعداد بازدید")

    # --- فیلدهای جدید اضافه شده برای رزرو و اقامتگاه ---
    price_per_night = models.PositiveIntegerField(default=0, verbose_name="قیمت هر شب (تومان)")
    city = models.CharField(max_length=100, default="نامشخص", verbose_name="شهر")
    bedrooms = models.PositiveSmallIntegerField(default=1, verbose_name="تعداد اتاق خواب")
    bathrooms = models.PositiveSmallIntegerField(default=1, verbose_name="تعداد سرویس بهداشتی")
    capacity_base = models.PositiveSmallIntegerField(default=2, verbose_name="ظرفیت پایه (نفر)")
    capacity_max = models.PositiveSmallIntegerField(default=4, verbose_name="حداکثر ظرفیت (نفر)")


    def __str__(self):
        return " {} - {}".format(self.title, self.id)
