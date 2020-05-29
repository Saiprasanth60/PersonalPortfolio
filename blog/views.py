from django.shortcuts import render, get_object_or_404
from .models import blog_data

# Create your views here.
def all_blog(request):
    project_blog_data = blog_data.objects.order_by()
    return render(request, 'blog.html', {'project_blog_data':project_blog_data})

def detail_view(request, blog_id):
    blog = get_object_or_404(blog_data, pk = blog_id)
    return render(request, 'detail_view.html', {'blog_dta':blog})