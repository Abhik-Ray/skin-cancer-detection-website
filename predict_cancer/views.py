from os import remove, path, listdir
from django.shortcuts import render
from predict_cancer.predict import predict
from tensorflow.keras import models
from django.core.files.storage import FileSystemStorage
# Create your views here.


def index(request):
    return render(request, "index.html")


def result(request):
    if request.POST:
        file = request.FILES["dataset"]
        fs = FileSystemStorage(location='./media')
        fs.save(file.name, file)
        model2 = models.load_model('./models/network.h5')
        p = predict(MEDIA_PATH='./media', model=model2)
        result = p.predict_value()
        for f in listdir('./media'):
            remove(path.join('./media', f))
        print(result)

    return render(request, "result.html")


def main(request):
    if request.FILES:
        file = request.FILES["dataset"]
        fs = FileSystemStorage(location='./media')
        fs.save(file.name, file)
        model2 = models.load_model('./models/network.h5')
        p = predict(MEDIA_PATH='./media', model=model2)
        try:
            result = p.predict_value()
        except:
            for f in listdir('./media'):
                remove(path.join('./media', f))
            return render(request, "main.html", {"percent": 0})
        for f in listdir('./media'):
            remove(path.join('./media', f))
        value = result[0] * 100
        value = "{:.2f}".format(value)
        value = float(value)
        return render(request, "main.html", {"percent": value})
    else:
        return render(request, "main.html", {"percent": 0})
