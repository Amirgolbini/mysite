from django.contrib import admin
from blog.models import Post, Reservation

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # published_date حذف شد و فیلدهای جدید جایگزین شدند
    list_display = ('title', 'city', 'price_per_night', 'status', 'created_date')
    list_filter = ('status', 'city')
    ordering = ('-created_date',)
    search_fields = ('title', 'content', 'city')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'post', 'check_in', 'check_out', 'total_price', 'created_at')
    list_filter = ('created_at', 'check_in')
    search_fields = ('full_name', 'phone_number', 'post__title')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)