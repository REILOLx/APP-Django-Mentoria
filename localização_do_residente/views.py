from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services import EnderecoServices,ResidenteServices
from .serializers import EnderecoSerializer,ResidenteSerializer


class EnderecoAPI(APIView):


    def get(self, request):
        enderecos = EnderecoServices.query_all()
        serializer = EnderecoSerializer(enderecos, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = EnderecoSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnderecoDetailAPI(APIView):


    def get(self, request, id_endereco):
        endereco = EnderecoServices.get(id_endereco)

        if endereco:
            serializer = EnderecoSerializer(endereco)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'erro':'endereço nao existe'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id_endereco):
        endereco = EnderecoServices.get(id_endereco)

        if endereco:
            endereco.delete()
            return Response(data={'delete':'endereço deletado'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'erro':'endereço nao existe'}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request, id_endereco):
        data = request.data
        endereco = EnderecoServices.get(id_endereco)

        if endereco:
            serializer = EnderecoSerializer(instance=endereco, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'erro':'endereço nao existe'}, status=status.HTTP_404_NOT_FOUND) 
        
class ResidenteAPI(APIView):


    def get(self, request):
        residentes = ResidenteServices.query_all()
        serializer = ResidenteServices(residentes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ResidenteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResidenteDetailAPI(APIView):


    def get(self, request, id_residente):
        residente = ResidenteServices.get(id_residente)

        if residente:
            serializer = ResidenteSerializer(residente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={'erro':'residente nao existe'}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, id_residente):
        residente = ResidenteServices.get(id_residente)

        if residente:
            residente.delete()
            return Response(data={'delete': 'residente deletado'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data={'erro': 'residente nao existe'}, status=status.HTTP_404_NOT_FOUND)

        
    def put(self, request, id_residente):
        data = request.data
        residente = ResidenteServices.get(id_residente)

        if residente:
            serializer = ResidenteSerializer(instance=residente, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'erro':'residente nao existe'}, status=status.HTTP_404_NOT_FOUND) 
        