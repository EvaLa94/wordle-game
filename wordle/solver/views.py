from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import FiveCharWord
from .serializers import FiveCharWordSerializer

# Create your views here.


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse('Please send a post request')

    if request.method == 'POST':
        data = JSONParser().parse(request)

        green_letters = data['green_letters']
        yellow_letters = data['yellow_letters']
        grey_letters = data['grey_letters']

        condition = Q(word__regex=r'{}'.format(green_letters))
        if yellow_letters:  # include letters
            condition &= Q(word__regex=r'[{}]'.format(yellow_letters))
        if grey_letters:  # exclude letters
            condition &= ~Q(word__regex=r'[{}]'.format(grey_letters))

        # FiveCharWord.objects.filter(condition)
        result = FiveCharWord.objects.filter(condition)
        serializer = FiveCharWordSerializer(result, many=True)
        return JsonResponse(serializer.data, safe=False)
