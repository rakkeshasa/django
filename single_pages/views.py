from django.shortcuts import render
from blog.models import Post
from single_pages.models import IntelCpu, amdCpu, nvidia, ram, radeon, hdd, ssd, intelMB, amdMB

def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]

    return render(
        request,
        'single_pages/landing.html',
        {
            'recent_posts': recent_posts,
        }
    )


def about_me(request):
    Intel = IntelCpu.objects.all()
    AMD = amdCpu.objects.all()
    NVIDIA = nvidia.objects.all()
    RAM = ram.objects.all()
    RADEON = radeon.objects.all()
    HDD = hdd.objects.all()
    SSD = ssd.objects.all()
    IntelMB = intelMB.objects.all()
    AMDMB = amdMB.objects.all()

    return render(
        request,
        'single_pages/products.html',
        {
            'intel': Intel,
            'amd': AMD,
            'nvidia': NVIDIA,
            'ram': RAM,
            'radeon': RADEON,
            'hdd': HDD,
            'ssd': SSD,
            'intelMB': IntelMB,
            'amdMB': AMDMB,
        }
    )
# Create your views here.
