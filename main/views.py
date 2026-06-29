from django.shortcuts import render, redirect
from django.views import View
import json
from .models import Record,Status,Type, Category, Subcategory
from .forms import RecordForm,StatusForm, TypeForm, CategoryForm, SubcategoryForm

# Create your views here.


class RecordsView(View):
    def get(self, request):
        records = Record.objects.all()
        date = request.GET.get("date")
        status = request.GET.get("status")
        category = request.GET.get("category")
        subcategory = request.GET.get("subcategory")
        if date:
            records = records.filter(date=date)
        if status:
            records = records.filter(status_id=status)

        if category:
            records = records.filter(category_id=category)
        if subcategory:
            records = records.filter(subcategory_id=subcategory)

        context = {
            "records": records,
            "statuses": Status.objects.all(),
            "categories": Category.objects.all(),
            "subcategories": Subcategory.objects.all(),
        }
        return render(request, "main/records.html", context)

class RecordsControlView(View):
    def get(self, request):
        form = RecordForm()
        context = {
            'form':form,
            'records':Record.objects.all(),
            'types': Type.objects.all(),
            'categories': Category.objects.all(),
            'subcategories': Subcategory.objects.all(),
            'categories_json': json.dumps(list(Category.objects.values('id', 'name', 'type_id'))),
            'subcategories_json': json.dumps(list(Subcategory.objects.values('id', 'name', 'category_id'))),
         }

        return render(request, "main/record_control.html", context)

    def post(self, request):
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("record_control")
        return render(request, "main/record_control.html", {"form": form})

class RecordEditView(View):
    
    def get(self,request,id):
       
        record_que = Record.objects.get(id=id)
        form = RecordForm(instance=record_que)
        context = {
            'form':form,
            'records':Record.objects.all(),
            'types': Type.objects.all(),
            'categories': Category.objects.all(),
            'subcategories': Subcategory.objects.all(),
            'categories_json': json.dumps(list(Category.objects.values('id', 'name', 'type_id'))),
            'subcategories_json': json.dumps(list(Subcategory.objects.values('id', 'name', 'category_id'))),
        }
        return render(request,'main/record_control__edit.html',context)

    def post(self,request,id):
        
        record_que = Record.objects.get(id=id)
        form = RecordForm(request.POST,instance=record_que)
        context = {
            'form':form,
            'records':Record.objects.all(),
            'types': Type.objects.all(),
            'categories': Category.objects.all(),
            'subcategories': Subcategory.objects.all(),
            'categories_json': json.dumps(list(Category.objects.values('id', 'name', 'type_id'))),
            'subcategories_json': json.dumps(list(Subcategory.objects.values('id', 'name', 'category_id'))),
         }
        if form.is_valid():
            form.save()
            return redirect('record_control')
        
        return render(request,'main/record_control__edit.html',context)

class RecordDeleteView(View):
    def post(self,request,id):
        record_que = Record.objects.get(id=id)
        record_que.delete()
        return redirect('record_control')
    
class CatalogControlView(View):
    def get(self, request):
        return render(
            request,
            "main/catalog_control.html",
            {
                "status_form":StatusForm(),
                "type_form": TypeForm(),
                "category_form": CategoryForm(),
                "subcategory_form": SubcategoryForm(),
                "statuses":Status.objects.all(),
                "subcategories": Subcategory.objects.all(),
                "types": Type.objects.all(),
                "categories": Category.objects.all(),
            },
        )

    def post(self, request):
        if "add_status" in request.POST:
            form = StatusForm(request.POST)
            if form.is_valid():
                form.save()

        elif "add_type" in request.POST:
            form = TypeForm(request.POST)
            if form.is_valid():
                form.save()

        elif "add_category" in request.POST:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()

        elif "add_subcategory" in request.POST:
            form = SubcategoryForm(request.POST)
            if form.is_valid():
                form.save()

        return redirect("catalog_control")

class StatusEditView(View):
    def get(self,request,id):
        status_que = Status.objects.get(id=id)
        form = StatusForm(instance=status_que)
        return render(request,'main/catalog_control__edit-status.html',{"form":form})

    def post(self,request,id):
        status_que = Status.objects.get(id=id)
        form = StatusForm(request.POST,instance=status_que)
        if form.is_valid():
            form.save()
            return redirect('catalog_control')
        
        return render(request,'main/catalog_control__edit-status.html',{"form":form})

class StatusDeleteView(View):
    def post(self,request,id):
        status_que = Status.objects.get(id=id)
        status_que.delete()
        return redirect('catalog_control')
    
class TypeEditView(View):
    def get(self,request,id):
        type_que = Type.objects.get(id=id)
        form = TypeForm(instance=type_que)
        return render(request,'main/catalog_control__edit-type.html',{"form":form})

    def post(self,request,id):
        type_que = Type.objects.get(id=id)
        form = TypeForm(request.POST,instance=type_que)
        if form.is_valid():
            form.save()
            return redirect('catalog_control')
        
        return render(request,'main/catalog_control__edit-type.html',{"form":form})

class TypeDeleteView(View):
    def post(self,request,id):
        type_que = Type.objects.get(id=id)
        type_que.delete()
        return redirect('catalog_control')
    
class CategoryEditView(View):
    def get(self,request,id):
        category_que = Category.objects.get(id=id)
        form = CategoryForm(instance=category_que)
        return render(request,'main/catalog_control__edit-category.html',{"form":form})

    def post(self,request,id):
        category_que = Category.objects.get(id=id)
        form = CategoryForm(request.POST,instance=category_que)
        if form.is_valid():
            form.save()
            return redirect('catalog_control')
        
        return render(request,'main/catalog_control-edit-category.html',{"form":form})

class CategoryDeleteView(View):
    def post(self,request,id):
        category_que = Category.objects.get(id=id)
        category_que.delete()
        return redirect('catalog_control')
    

class SubcategoryEditView(View):
    def get(self,request,id):
        subcategory_que = Subcategory.objects.get(id=id)
        form = SubcategoryForm(instance=subcategory_que)
        return render(request,'main/catalog_control__edit-subcategory.html',{"form":form})

    def post(self,request,id):
        subcategory_que = Subcategory.objects.get(id=id)
        form = SubcategoryForm(request.POST,instance=subcategory_que)
        if form.is_valid():
            form.save()
            return redirect('catalog_control')
        
        return render(request,'main/catalog_control-edit-subcategory.html',{"form":form})

class SubcategoryDeleteView(View):
    def post(self,request,id):
        subcategory_que = Subcategory.objects.get(id=id)
        subcategory_que.delete()
        return redirect('catalog_control')
    
