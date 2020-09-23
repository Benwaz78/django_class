from frontend.models import Category
import datetime

def menu_cat(request):
    cat = Category.objects.all()
    return {'cat':cat}

def post_data(request):
    dat = datetime.datetime.now()
    return {'d':dat}