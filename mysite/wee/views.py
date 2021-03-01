from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Washroom
from .forms import PostForm
from django.utils import timezone
from .models import Post
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

longitude = -122.55465
latitude = 49.163635

user_location = Point(longitude, latitude, srid=4326)

# Create your views here.
def index(request):
  context = {"home_page": "active"}
  return render(request, 'wee/index.html', context)

def about(request):
  context = {"about_page": "active"}
  return render(request, 'wee/about.html', context)

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'wee/post_list.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'wee/post_edit.html', {'form': form})

def washroom_detail(request, pk):
    washrooms = get_object_or_404(Washroom, pk=pk)
    return render(request, 'wee/washroom_detail.html', {'washrooms': washrooms})

    
@login_required
def review_washroom(request, pk):
    washrooms = get_object_or_404(Washroom, pk=pk)
    return render(request, 'wee/review_washroom.html', {'washrooms': washrooms})

# @method_decorator(login_required, name='dispatch')
# @login_required
def Home(request):
    model = Washroom

    if request.method == "POST":
        type = request.POST.get('type')
        water = request.POST.get('water')
        wheelchair = request.POST.get('wheelchair')
        indoor = request.POST.get('indoor')
        access = request.POST.get('access')
        diaper = request.POST.get('diaper')
        unisex = request.POST.get('unisex')

        qs = Washroom.objects.all()

        if (type!="Type unknown"):
            qs = qs.filter(type=type)

        if (water!="False"):
            qs = qs.filter(water=water)

        if (wheelchair!="False"):
            qs = qs.filter(wheelchair=wheelchair)

        if (indoor!="False"):
            qs = qs.filter(indoor=indoor)

        if (access!="False"):
            qs = qs.filter(access=access)

        if (diaper!="False"):
            qs = qs.filter(diaper=diaper)

        if (unisex!="False"):
            qs = qs.filter(unisex=unisex)

        qs = qs.annotate(
            distance = Distance("location", user_location)
        ).order_by("distance")
        context = {
            'queryset':qs
        }

        return render(request, 'wee/index.html', context)
    else:
        qs = Washroom.objects.annotate(
            distance = Distance("location", user_location)
        ).order_by("distance")

        context = {
            'queryset':qs
        }

        return render(request, 'wee/index.html', context)
