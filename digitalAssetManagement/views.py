from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    return render(request, 'index.html')

def describeImages(request):
    # 1) Récupération des données depuis le form
    if request.method == 'POST':
        postData = request.POST['email']

    # 2) Requete API pour récupérer les données de L'IA Azure

    data = ['38%','Un mec en skate', 'https://www.grapheine.com/wp-content/uploads/2015/09/nouveau-logo-google-2015.jpg']

    # 3) Récupération des données et render sur la template HTML
    return render(request, 'describe.html', dict(data=data))