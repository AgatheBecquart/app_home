from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from website.forms import ContactUsForm, PredictionForm
from . import forms
from .models import *
import pandas as pd 

def welcome(request):
    return render(request, 'website/welcome.html')

@login_required
def home(request):
    return render(request, 'website/home.html')

def contact(request):
    """Cette fonction gère la vue de la page de contact du système.

    Elle utilise le formulaire ContactUsForm pour collecter les informations de l'utilisateur et les envoyer au serveur pour traitement.

    Paramètres :
    - request (HttpRequest) : L'objet de requête HTTP envoyé par le client.
    """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

    else:
        form = ContactUsForm()

    return render(request,
                'website/contact.html',
                {'form': form})

def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'website/signup.html', context={'form': form})

def about(request):
    return render(request, 'website/about.html')

def consult(request):
    predictions = Prediction.objects.filter(user=request.user)
    return render(request, 'website/consult.html', {'predictions':predictions})

import pickle
"""
    Le code ci-dessus ouvre un fichier binaire contenant un objet de pipeline d'apprentissage automatique entraîné à l'aide du module pickle de Python. L'argument 'rb' spécifie que le fichier doit être ouvert en mode lecture binaire.
    Une fois que le fichier est ouvert, la méthode pickle.load() est utilisée pour charger le contenu du fichier dans un objet Python.
"""

with open('website/trained_pipeline_v2.pkl', 'rb') as file:
    model = pickle.load(file)
    


def estimate(request):
    """
    Vue qui permet d'estimer le prix d'une maison en utilisant un modèle de machine learning. Les données sont entrées via un formulaire et utilisées pour faire une prédiction. L'utilisateur a la possibilité d'enregistrer la prédiction sur le site.

    Args:
    request (HttpRequest): Requête HTTP reçue par la vue.

    Returns:
    HttpResponse: Réponse HTTP retournée par la vue.
    """
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            action = request.POST.get('action_type') 
            # Obtenez les valeurs entrées par l'utilisateur
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            m2_living = form.cleaned_data['m2_living']
            m2_lot = form.cleaned_data['m2_lot']
            floors = form.cleaned_data['floors']
            waterfront = form.cleaned_data['waterfront']
            view = form.cleaned_data['view']
            condition = form.cleaned_data['condition']
            grade = form.cleaned_data['grade']
            m2_above = form.cleaned_data['m2_above']
            yr_built = form.cleaned_data['yr_built']
            zipcode = form.cleaned_data['zipcode']
            has_basement = form.cleaned_data['has_basement']
            was_renovated = form.cleaned_data['was_renovated']

            # Préparez les données pour la prédiction
            X = pd.DataFrame({'bedrooms': [bedrooms],
                              'bathrooms': [bathrooms],
                              'm2_living': [m2_living],
                              'm2_lot': [m2_lot],
                              'floors': [floors],
                              'waterfront': [waterfront],
                              'view': [view],
                              'condition': [condition],
                              'grade': [grade],
                              'm2_above': [m2_above],
                              'yr_built': [yr_built],
                              'zipcode': [zipcode],
                              'has_basement': [has_basement],
                              'was_renovated': [was_renovated],
                              })

            # Utilisez le modèle pour faire une prédiction
            y_pred = model.predict(X)

            # Vérifiez si l'utilisateur a appuyé sur le bouton "Enregistrer"
            if action == 'predict':
                prediction = "{:,.0f}".format(y_pred[0]).replace(",", " ")
                context = {'form': form, 'prediction': prediction}
                return render(request, 'website/estimate.html', context=context)
            if action == 'save_prediction':
                prediction = form.save(commit=False)
                prediction.user = request.user
                prediction.predicted_price = round(y_pred[0])
                prediction.full_clean()
                prediction.save()
                # Redirigez vers la page de détail de prédiction
                return redirect('consult')
    else:
        form = PredictionForm()
    context = {'form': form}
    return render(request, 'website/estimate.html', context=context)


@login_required
def prediction_detail(request, id):
    """
    Vue qui affiche les détails d'une prédiction enregistrée sur le site. L'utilisateur doit être connecté pour accéder à cette vue.

    Args:
    request (HttpRequest): Requête HTTP reçue par la vue.
    id (int): Identifiant de la prédiction à afficher.

    Returns:
    HttpResponse: Réponse HTTP retournée par la vue, contenant les détails de la prédiction demandée.
    """
    prediction = get_object_or_404(Prediction, id=id)
    return render(request, 'website/prediction_detail.html', {'prediction':prediction})

@login_required
def prediction_change(request, id):
    """
    Cette vue permet à l'utilisateur connecté de modifier une prédiction existante en utilisant un formulaire. Les données saisies par l'utilisateur sont utilisées pour faire une nouvelle prédiction de prix à l'aide d'un modèle. La prédiction mise à jour est enregistrée dans la base de données et l'utilisateur est redirigé vers la page de détails de la prédiction.

    Args:
    request (HttpRequest): La requête HTTP reçue par la vue.

    Returns:
    HttpResponse: Une réponse HTTP qui peut être rendue par le navigateur. Cette réponse contient le formulaire pour modifier la prédiction et affiche les erreurs de validation si elles existent. Si le formulaire est validé avec succès, l'utilisateur est redirigé vers la page de détails de la prédiction.
    """
    prediction = Prediction.objects.get(id=id)
    if request.method == 'POST':
        form = PredictionForm(request.POST, instance=prediction)
        if form.is_valid():
            # Obtenez les valeurs de formulaire entrées par l'utilisateur
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            m2_living = form.cleaned_data['m2_living']
            m2_lot = form.cleaned_data['m2_lot']
            floors = form.cleaned_data['floors']
            waterfront = form.cleaned_data['waterfront']
            view = form.cleaned_data['view']
            condition = form.cleaned_data['condition']
            grade = form.cleaned_data['grade']
            m2_above = form.cleaned_data['m2_above']
            yr_built = form.cleaned_data['yr_built']
            zipcode = form.cleaned_data['zipcode']
            has_basement = form.cleaned_data['has_basement']
            was_renovated = form.cleaned_data['was_renovated']

            # Préparez les données pour la prédiction
            X = pd.DataFrame({'bedrooms': [bedrooms],
                              'bathrooms': [bathrooms],
                              'm2_living': [m2_living],
                              'm2_lot': [m2_lot],
                              'floors': [floors],
                              'waterfront': [waterfront],
                              'view': [view],
                              'condition': [condition],
                              'grade': [grade],
                              'm2_above': [m2_above],
                              'yr_built': [yr_built],
                              'zipcode': [zipcode],
                              'has_basement': [has_basement],
                              'was_renovated': [was_renovated],
                              })

            # Utilisez le modèle pour faire une prédiction
            y_pred = model.predict(X)

            # Mettez à jour le prix prédit dans la base de données
            prediction = form.save(commit=False)
            prediction.user = request.user
            prediction.predicted_price = round(y_pred[0])
            prediction.full_clean()
            prediction.save()
            
            return redirect('prediction-detail', id) 
        elif not form.is_valid():
            form = PredictionForm(instance=prediction)
    else:
        form = PredictionForm(instance=prediction)
    return render(request,
                    'website/prediction_change.html',
                    {'form': form})

 
@login_required   
def prediction_delete(request, id):
    """
    Cette vue permet à l'utilisateur connecté de supprimer une prédiction existante en utilisant un formulaire de confirmation. Si l'utilisateur confirme la suppression, la prédiction est supprimée de la base de données et l'utilisateur est redirigé vers la page de consultation des prédictions.

    Args:
    request (HttpRequest): La requête HTTP reçue par la vue.

    Returns:
    HttpResponse: Une réponse HTTP qui peut être rendue par le navigateur. Cette réponse contient le formulaire de confirmation pour supprimer la prédiction. Si l'utilisateur confirme la suppression, il est redirigé vers la page de consultation des prédictions. Sinon, la page de confirmation de suppression est affichée à nouveau.
    """
    prediction = Prediction.objects.get(id=id)

    if request.method == 'POST':
        prediction.delete()
        return redirect('consult') 
    return render(request,
                    'website/prediction_delete.html',
                    {'prediction': prediction})