from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def users_list(request):
    # Créer une liste d'utilisateurs fictifs
    users = [
        {"first_name": "Alice", "last_name": "Smith"},
        {"first_name": "Bob", "last_name": "Brown"},
        {"first_name": "Charlie", "last_name": "Johnson"},
        {"first_name": "David", "last_name": "Lee"},
        {"first_name": "Eve", "last_name": "Williams"},
    ]
    # Retourner la réponse JSON avec les utilisateurs
    return Response(users)
