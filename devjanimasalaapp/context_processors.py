from .models import Category

def category(request):
    category = Category.objects.all()
    return {"Category":category}