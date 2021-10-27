from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import StoreEvent
from .serializers import EventSerializer, AddUpdateListEventSerializer
from datetime import datetime


class ViewAllEvents(ListAPIView):
    serializer_class = AddUpdateListEventSerializer

    def get_queryset(self):
        now = datetime.now()

        return StoreEvent.objects.filter(end_date__gte=now).order_by('start_date')


class CreateEvent(CreateAPIView):
    serializer_class = AddUpdateListEventSerializer
    
    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = self.perform_create(serializer)
            instance_serializer = EventSerializer(instance)
            return Response(instance_serializer.data)
        return Response(serializer.errors)


class ViewSingleEvent(RetrieveUpdateDestroyAPIView):

    def get(self, request, pk):
        post = StoreEvent.objects.get(pk=pk)
        serializer = EventSerializer(post, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = StoreEvent.objects.get(pk=pk)
        serializer = AddUpdateListEventSerializer(
            event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        event = StoreEvent.objects.get(pk=pk)
        event.delete()
        return Response(status=status.HTTP_200_OK)
