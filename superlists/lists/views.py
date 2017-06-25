# Create your views here.
from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    # return render(request, 'home.html', {
    #     'new_item_text' : request.POST.get('item_text',''),
    # })
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    if request.method == 'POST':
        # new_item_text = request.POST['item_text']

        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    return render(request, 'home.html')
    # else:
    #     new_item_text = ''
    #
    # return render(request, 'home.html', {
    #     'new_item_text': new_item_text,
    # })
