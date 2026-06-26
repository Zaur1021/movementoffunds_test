from django.shortcuts import render,redirect
from django.views import View
from .forms import RecordForm
# Create your views here.

class RecordsView(View):
    def get(self,request):
            return render(request,'main/records.html')

class RecordsControlView(View):
    def get(self,request):
        form = RecordForm()
        return render(request,'main/record_control.html',{'form' : form})
    
    def post(self,request):
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records')
        return render(request,'main/record_control.html',{'form' : form})

class CatalogControlView(View):
    def get(self,request):
        return render(request,'main/catalog_control.html')