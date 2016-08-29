from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from .forms import ProcessImageForm
from .models import Image
from .utils import convert_image_to_greyscale, resize_image


class ProcessImageView(View):
    """docstring for ProcessImage"""
    def get(self, request, *args, **kwargs):
        form = ProcessImageForm()
        return render(request, 'base.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProcessImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image.objects.create(img=request.FILES.get('image'))
            convert_image_to_greyscale(image.img)
            resize_image(image.img, height=256, width=256)
            return HttpResponseRedirect(
                reverse('core:image_detail', kwargs={'image_id': image.id})
            )
        else:
            return render(request, 'base.html', {'form': form})


class ImageDetailView(View):
    """docstring for ImageDetailView"""
    def get(self, request, *args, **kwargs):
        image_id = kwargs.get('image_id')
        image = Image.objects.get(id=image_id)
        form = ProcessImageForm()
        context = {
            'form': form,
            'original_path': image.img.url,
            'greyscale_path': image.greyscale_path,
            'resize_path': image.resize_path,
            'image_data': {
                'file_name': image.img.name.split("/")[-1],
                'dimensions': (image.img.height, image.img.width),
                'file_size': image.img.size,
                'file_type': image.img.name.split(".")[-1]
            },
        }
        return render(request, 'detail.html', context)
