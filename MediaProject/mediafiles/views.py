from django.shortcuts import render
from .models import Media

def media_list(request):
    all_media = Media.objects.all()
    audio_files = Media.objects.audio()
    video_files = Media.objects.video()
    image_files = Media.objects.images()

    context = {
        'all_media': all_media,
        'audio_files': audio_files,
        'video_files': video_files,
        'image_files': image_files,
    }
    return render(request, 'mediafiles/media_list.html', context)
