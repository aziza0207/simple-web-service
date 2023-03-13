from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from products.models import Version
from products.serializers import VersionSerializer, VersionDetailSerializer


class ListCreateVersion(APIView):
    def get(self, request):
        versions = Version.objects.all()
        serializer = VersionSerializer(versions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VersionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VersionDetail(APIView):
    def get_object(self, pk):
        try:
            return Version.objects.get(pk=pk)
        except Version.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        version = self.get_object(pk)
        serializer = VersionDetailSerializer(version)
        return Response(serializer.data)

    def put(self, request, pk):
        version = self.get_object(pk)
        serializer = VersionDetailSerializer(version, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        version = self.get_object(pk)
        version.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
