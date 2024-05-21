import json
from django.http import JsonResponse
from .models import GoogleAccount
from rest_framework.decorators import api_view

@api_view(['POST'])
def submit_google_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email=data['email']
        password = data['password']
        if email and password:
            account = GoogleAccount(email=email, password=password)
            account.save()
            return JsonResponse({'message': 'Google account details saved successfully.'})
        else:
            return JsonResponse({'error': 'Email and password are required.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)




# def get_google_account(request):
#     GoogleAccount.objects.all(email = email)
@api_view(['GET'])
def get_google_account(request):
    if request.method == 'GET':
        # Retrieve all GoogleAccount objects
        google_accounts = GoogleAccount.objects.all()

        # Serialize the data
        serialized_data = [{'email': account.email, 'password': account.password} for account in google_accounts]
        print(serialized_data)
        return JsonResponse(serialized_data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)
