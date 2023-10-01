from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import glob
import os
from  inference import *


@csrf_exempt
def index(request):
    if request.method == "POST" and request.FILES['file']:
        file = request.FILES.get('file')
        input_img = glob.glob('static/input_img/*')
        for f in input_img:
            os.remove(f)
        folder_path = 'static/input_img/'
        url = request.get_host()

        location = FileSystemStorage(location=folder_path)
        fn = location.save(file.name, file)
        path = os.path.join(folder_path, fn)
        # frame = cv2.imread(path)
        image_path = main_fun(path)
        context = {
            "status": 'Sucess',
            "image_path": f'{url}/{image_path}',
        }
        return JsonResponse(context)
    else:
        context = {
            "Error": 'Send valid request',
        }
        return JsonResponse(context)
        

   

