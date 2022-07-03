from django.shortcuts import render, get_object_or_404, redirect

def index(request):
    return render(request, 'index.html')

def describeImages(request):
    # 1) Récupération des données depuis le form
    if request.method == 'POST':
        titreImg = request.POST['titreImg']
        fileImg = request.POST['fileImg']
        tag = request.POST['tag']
        flexProduit = request.POST['flexProduit']
        precisionProduit = request.POST['precisionProduit']
        flexHumain = request.POST['flexHumain']
        typologie = request.POST['typologie']
        action = request.POST['action']
        DescriptionExt = request.POST['DescriptionExt']
        flexFormat = request.POST['flexFormat']
        precisionFormat = request.POST['precisionFormat']
        saisieLibre = request.POST['saisieLibre']
        flexlogo = request.POST['flexlogo']
        Cibles = request.POST['Cibles']
    # 2) Requete API pour récupérer les données de L'IA Azure

    data = ["Cibles :"+Cibles,"flexlogo :"+flexlogo,"titreImg :"+titreImg,"fileImg :"+fileImg,"precisionProduit :"+precisionProduit,"Tag :"+tag,"Produit :"+flexProduit,"Humain :"+flexHumain,"typologie :"+typologie,"action :"+action,"DescriptionExt :"+DescriptionExt,"flexFormat :"+flexFormat,"precisionFormat :"+precisionFormat,"saisieLibre :"+saisieLibre]

    # 3) Récupération des données et render sur la template HTML
    return render(request, 'describe.html', dict(data=data))