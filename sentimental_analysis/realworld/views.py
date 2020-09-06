from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def analysis(request):
    note = "Hello"
    return render(request,'realworld/analysis.html',{'note':note})

def input(request):
    if request.method=='POST':
        name = request.POST.get("Name", "")
        file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(file.name,file)
    else:
        note = "Please Enter the file you want it to be uploaded"
        return render(request, 'realworld/home.html', {'note': note})

def productanalysis(request):
    if request.method=='POST':
        blogname = request.POST.get("blogname", "")
        print(blogname)
    else:
        note = "Please Enter the product blog name for analysis"
        return render(request, 'realworld/productanalysis.html', {'note': note})
