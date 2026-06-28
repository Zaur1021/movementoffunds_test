from django.shortcuts import render, redirect
from django.views import View
from .models import Type, Category, Subcategory
from .forms import RecordForm, TypeForm, CategoryForm, SubcategoryForm

# Create your views here.


class RecordsView(View):
    def get(self, request):
        return render(request, "main/records.html")


class RecordsControlView(View):
    def get(self, request):
        form = RecordForm()
        return render(request, "main/record_control.html", {"form": form})

    def post(self, request):
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("records")
        return render(request, "main/record_control.html", {"form": form})


class CatalogControlView(View):
    def get(self, request):
        return render(
            request,
            "main/catalog_control.html",
            {
                "type_form": TypeForm(),
                "category_form": CategoryForm(),
                "subcategory_form": SubcategoryForm(),
                "subcategories": Subcategory.objects.all(),
                "types": Type.objects.all(),
                "categories": Category.objects.all(),
            },
        )

    def post(self, request):
        if "add_type" in request.POST:
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
    
