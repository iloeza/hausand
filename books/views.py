from django.shortcuts import render
from .models import Book

# Create your views here.
def home(request):
    return render(request, 'books/home.html')

def maternal(request):
    maternal_books = Book.objects.filter(nivel="maternal", status=True)
    if request.method == "POST":
        book = Book.objects.get(pk=request.POST['bookId'])
        book.status=False
        book.telefono_responsable = request.POST['telefono_responsable']
        book.email_responsable = request.POST['email_responsable']
        book.responsable = request.POST['alumno_responsable']
        book.save()
    return render(request, 'books/maternal.html', {"books": maternal_books})

def kinder(request):
    kinder_books = Book.objects.filter(nivel="kinder", status=True)
    if request.method == "POST":
        book = Book.objects.get(pk=request.POST['bookId'])
        book.status=False
        book.telefono_responsable = request.POST['telefono_responsable']
        book.email_responsable = request.POST['email_responsable']
        book.responsable = request.POST['alumno_responsable']
        book.save()
    return render(request, 'books/kinder.html', {"books": kinder_books})

def primaria(request):
    primaria_books = Book.objects.filter(nivel="primaria", status=True)
    if request.method == "POST":
        book = Book.objects.get(pk=request.POST['bookId'])
        book.status=False
        book.telefono_responsable = request.POST['telefono_responsable']
        book.email_responsable = request.POST['email_responsable']
        book.responsable = request.POST['alumno_responsable']
        book.save()
    return render(request, 'books/primaria.html', {"books": primaria_books})