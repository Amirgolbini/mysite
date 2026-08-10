from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from blog.models import Post, Reservation
from datetime import datetime

# Create your views here.
def blog_view(request):
    return render(request, 'blog/blog-home.html')


def blog_single(request):
    return render(request, 'blog/blog-single.html')

def reserve_view(request):
    return render(request, 'website/reserve.html')





def reservation_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=True)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        check_in_str = request.POST.get('check_in')
        check_out_str = request.POST.get('check_out')

        if full_name and phone_number and check_in_str and check_out_str:
            try:
                check_in = datetime.strptime(check_in_str, '%Y-%m-%d').date()
                check_out = datetime.strptime(check_out_str, '%Y-%m-%d').date()

                nights = (check_out - check_in).days
                if nights <= 0:
                    messages.error(request, 'تاریخ خروج باید بعد از تاریخ ورود باشد.')
                else:
                    total_price = nights * post.price_per_night
                    Reservation.objects.create(
                        post=post,
                        full_name=full_name,
                        phone_number=phone_number,
                        check_in=check_in,
                        check_out=check_out,
                        total_price=total_price
                    )
                    messages.success(request, 'درخواست رزرو شما با موفقیت ثبت شد. به‌زودی با شما تماس خواهیم گرفت.')
                    return redirect('blog:reservation_detail', post_id=post.id)
            except ValueError:
                messages.error(request, 'فرمت تاریخ نامعتبر است.')
        else:
            messages.error(request, 'لطفا تمامی فیلدها را به درستی تکمیل کنید.')

    # افزایش تعداد بازدید
    post.counted_views += 1
    post.save()

    context = {
        'post': post
    }

    return render(request, 'blog/reservation.html', context)