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
                "subcategory": Subcategory.objects.all(),
                "type": Type.objects.all(),
                "category": Category.objects.all(),
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
    