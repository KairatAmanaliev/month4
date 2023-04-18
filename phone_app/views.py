from django.shortcuts import render, get_object_or_404

from book.models import Phone


# Create your views here.
def phone_all_view(request):
    phone_list = Phone.objects.all()
    context = {
        'phone_list': phone_list
    }
    return render(request, 'phone-list.html', context)


# Подробная информация
def phone_detail_view(request, id):
    phone_id = get_object_or_404(Phone, id=id)
    context = {
        'phone_id': phone_id
    }
    return render(request, 'phone_detail.html', context)
