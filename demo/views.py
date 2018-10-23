from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

# Create your views here.
from rest_framework.parsers import JSONParser

from api.serializers import UserSerializer, GroupSerializer
from demo.models import Home, HomeSections, Articles
from demo.serializers import HomeSerializer, HomeSectionsSerializer, SectionsArticlesSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class HomesViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class HomesSectionsViewSet(viewsets.ModelViewSet):
    queryset = HomeSections.objects.all()
    serializer_class = HomeSectionsSerializer


class SectionsArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = SectionsArticlesSerializer


@csrf_exempt
def home_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        home = Home.objects.get(pk=pk)
    except Home.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HomeSerializer(home)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HomeSerializer(home, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        home.delete()
        return HttpResponse(status=204)
