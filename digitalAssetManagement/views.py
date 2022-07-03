from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    return render(request, 'index.html')

def describeImages(request):
    # 1) Récupération des données depuis le form
    if request.method == 'POST':
        titreImg = request.POST['titreImg']
        fileImg = request.POST['fileImg']

    # 2) Requete API pour récupérer les données de L'IA Azure

    data = [titreImg,fileImg]

    # 3) Récupération des données et render sur la template HTML
    return render(request, 'describe.html', dict(data=data))