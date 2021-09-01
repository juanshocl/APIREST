from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Persona, usuario
from .serializers import PersonaSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.hashers import check_password
from rest_framework import viewsets
from .serializers import UserSerializer

@api_view(['POST'])
def login(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('Usuario o contraseña no valido')
        
    pwd_valid = check_password(password,user.password)
    
    if not pwd_valid:
        return Response('contraseña no valido')
        
    token, _ = Token.objects.get_or_create(user=user)
    return Response(token.key, 'holi')
    # return render(request,'login.html' )

# class Login(FormView):
#     template_name = "login.html"
#     form_class = AuthenticationForm
#     success_url = reverse_lazy('persona_list')

#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self,request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return super(Login,self).dispatch(request,*args,*kwargs)

#     def form_valid(self,form):
#         user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
#         token,_ = Token.objects.get_or_create(user = user)
#         if token:
#             login(self.request, form.get_user())
#             return super(Login,self).form_valid(form)
    
#    ######### # Register API
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(user)[1]
#         })
    
    
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)