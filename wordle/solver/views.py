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

        result_regex = data['result_regex']

        condition = Q(word__regex=r'{}'.format(result_regex))

        for letter in data['must_include']:
            condition &= Q(word__contains=letter)

        # FiveCharWord.objects.filter(condition)
        result = FiveCharWord.objects.filter(condition)
        serializer = FiveCharWordSerializer(result, many=True)
        return JsonResponse(serializer.data, safe=False)
