import re

import os
from django.db.models import Q, F
from django.shortcuts import render, redirect

from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, FormView, DeleteView

from HomeworkDjango.models import Shop, Department, Item
from django.db.models import Min, Max, Avg, Count

from HomeworkDjango.utils import upload_file
from datetime import datetime

from HomeworkDjango.forms import SimpleForm, ItemCreateForm, SearchForm


def main(request):
    shops_all = Shop.objects.all()
    return render(request, 'main.html', {'shops_all': shops_all})


def select_data(request):
    items_desc = Item.objects.exclude(description__isnull=True).all()
    sphere_200 = Department.objects.filter(staff_amount__gt=200).all().values(
        'sphere').distinct()
    name_i = Shop.objects.filter(name__istartswith='i').all().values('address')
    items_furniture = Item.objects.filter(department__sphere='Furniture').all()
    shops_desc = Shop.objects.filter(
        departments__items__description__isnull=False).all().distinct()
    tuples = Item.objects.all()
    lst_items = [(i.name, i.department.sphere, i.department.shop.name) for i in
                 tuples]
    ordered_items = Item.objects.order_by('name').all()[1:4]
    ordered_items = [i.id for i in ordered_items]
    
    aggregated = Item.objects.values('department__shop').annotate(
        amount=Count('id'), max=Max('price'), min=Min('price'),
        avg=Avg('price')).filter(amount__gt=1).all()
    dict_new = {1: items_desc, 2: sphere_200, 3: name_i, 4: items_furniture,
                5: shops_desc, 6: lst_items, 7: ordered_items, 8: aggregated}
    return render(request, 'select_data.html', {'dict_new': dict_new})


def update_data(request):
    Item.objects.filter(Q(name__startswith='B') | Q(name__endswith='e')).update(
        price=F('price') + 100)
    return main(request)


def delete_data(request):
    Item.objects.filter((Q(price__gt=500) & Q(description__isnull=True)) | Q(
        department__shop__address__isnull=True)).delete()
    return main(request)


# def my_view(request, *args):
#      method=request.method #'GET', 'POST', 'PUT'
#      url_param = request.GET
#      post_body = request.POST
#      request.content_type

# def my_view(request, *args):
#     if request.method == 'GET':
#         context = {'departments':Department.objects.select_related('shop')}
#         return render(request, 'my_form.html', context)
#     elif request.method == 'POST':
#        Item.objects.create(name=request.POST.get("name"),
#                            description = request.POST.get("description"),
#                            price = int(request.POST.get("price")),
#                            department_id= request.POST.get("department"))
#        return redirect('index')


class MyView(View):

    def get(self, request):
        context = {'departments': Department.objects.select_related('shop')}
        return render(request, 'my_form.html', context)

    def post(self, request):
        item = Item.objects.create(name=request.POST.get("name"),
                                   description=request.POST.get("description"),
                                   price=int(request.POST.get("price")),
                                   department_id=request.POST.get("department"))
        image = upload_file(request.FILES['image'])
        item.image.save('{}.png'.format(item.id), image)
        return redirect('index')


def shops(request):
    return main(request)


class AddShop(TemplateView):
    template_name = "add_shop.html"

    def post(self, request):
        Shop.objects.create(name=request.POST.get("name"),
                            address=request.POST.get("address"),
                            staff_amount=int(request.POST.get("staff_amount")))
        return redirect('index')


def about_shop(request, shop_id):
    try:
        context = {'shops': Shop.objects.get(id=shop_id)}
    except Shop.DoesNotExist:
        return redirect('index')
    return render(request, 'about_shops.html', context)


class NewDep(View):

    def get(self, request, shop_id):
        return render(request, 'new_dep.html', {"shop_id": shop_id})

    def post(self, request, shop_id, is_name_invalid=False):
        if re.match(r'^[a-zA-zа-яА-я\s-]+$',
                    str(request.POST.get("sphere")),
                    flags=re.MULTILINE) is None:
            is_name_invalid = True
            context = {"sphere": request.POST.get("sphere"),
                       "description": request.POST.get("description"),
                       "staff_amount": request.POST.get("staff_amount"),
                       "is_name_invalid": is_name_invalid}
            return render(request, 'new_dep.html', context)
        else:
            Department.objects.create(sphere=request.POST.get("sphere"),
                                      description=request.POST.get(
                                          "description"),
                                      staff_amount=int(
                                          request.POST.get("staff_amount")),
                                      shop=Shop.objects.get(id=shop_id))
            return redirect('index')


class EditItem(TemplateView):
    template_name = "edit_item.html"

    def get_context_data(self, item_id, **kwargs):
        context = super(EditItem, self).get_context_data(**kwargs)
        context['items'] = Item.objects.get(id=item_id)
        return context

    def post(self, request, item_id):
        if request.POST.get("delete_image") == "on":
            Item.objects.filter(id=item_id).update(
            name=request.POST.get("name"),
            description=request.POST.get("description"),
            price=int(request.POST.get("price")),
            department_id=int(request.POST.get("department")))
            Item.objects.get(id=item_id).image.delete()
            return redirect('index')
        else:
            if 'image' in request.FILES:
                image = upload_file(request.FILES['image'])
                Item.objects.get(id=item_id).image.save(
                        '{}.png'.format(item_id), image)
                Item.objects.filter(id=item_id).update(
                    name=request.POST.get("name"),
                    description=request.POST.get("description"),
                    price=int(request.POST.get("price")),
                    department_id=int(request.POST.get("department")))
            return redirect('index')


def delete_object(request,item_id):
    Item.objects.get(id=item_id).delete()
    return redirect('index')


def template(request):
    current_date = datetime.now()
    number_1 = 9
    number_2 = 1.23456
    number_3 = 21
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dict =  {'a': 1, 'b': 2, 'c': 3}
    return render(request, 'numbers.html', {
        'current_date': current_date,
        'number_1': number_1,
        'number_2': number_2,
        'number_3': number_3,
        'array': array,
        'dict': dict
    })


class ItemCreateView(CreateView):
    template_name = 'create_item.html'
    success_url = '/'
    model = Item
    form_class = ItemCreateForm

    def get_context_data(self, **kwargs):
        context = super(ItemCreateView, self).get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        return context

    def form_valid(self, form):
        model = form.save(commit=False)
        return super(ItemCreateView, self).form_valid(form)


class ItemUpdate(UpdateView):
    model = Item
    template_name = 'update_item_new.html'
    form_class = ItemCreateForm
    success_url = '/'

    def form_valid(self, form):
        pk = self.request.POST.get('pk')
        image_delete = self.request.POST.get('delete_image')

        if image_delete == 'on':

            if self.object.image:

                os.remove(self.object.image.path)
                self.object.image = None

            else:
                pass

        elif image_delete is None:
            if self.object.image is None:
               pass

            else:
                item_id = form.instance.id
                item = Item.objects.filter(id=item_id).first()
                if item.image:
                   os.remove(item.image.path)
        return super(ItemUpdate, self).form_valid(form)


class Search(FormView):
    template_name = 'search.html'
    form_class = SearchForm

    def form_valid(self, form):
        data = form.cleaned_data
        result = Item.objects.filter(is_sold=data['is_sold'])
        if data['min_price']:
            result = result.filter(price__gte=data['min_price'])
        if data['max_price']:
            result = result.filter(price__lte=data['max_price'])
        if data['part_name']:
            result = result.filter(name__contains=data['part_name'])
        if data['shop']:
            result = result.filter(department__shop=data['shop'])

        return render(self.request, 'search_result.html', {'items':result})


class ItemDelete(DeleteView):
    model = Item
    success_url = '/'
    template_name = 'delete_item.html'
