from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import mixins, viewsets, parsers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.views import APIView

from django_test.serializers import UserSerializer


# REST API
class UserList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class CurrentUserDetail(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer

class CustomSchema(AutoSchema):
    def get_operation_id(self, path, method):
        return 'retrieveCurrentUser'


class CurrentUserDetail(APIView):
    schema = CustomSchema()
    # we must add this property otherwise the OpenAPI schema will
    # assume this path returns an array of objects
    # see is_list_view in rest_framework/schemas/utils.py
    action = 'retrieve'

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def get_serializer(self, *args, **kwargs):
        return UserSerializer(*args, **kwargs)


# We must redefine the parse_classes otherwise the generated JS client is wrong,
# it will generate methods to submit Form Data instead of JSON
class CustomObtainAuthToken(ObtainAuthToken):
    parser_classes = (parsers.JSONParser,)


# HTML
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog:index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def profile(request):
    return render(request, 'registration/profile.html')
