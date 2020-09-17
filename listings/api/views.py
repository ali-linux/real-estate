from rest_framework import generics
from listings.models import Listing 
from .serializers import ListingSerializer 
#from rest_framework.response import Response
#from rest_framework.views import APIView


class ListingListApiView(generics.ListAPIView):
    Permission_classes      = []
    authentication_classes  = []
    serializer_class        = ListingSerializer
    
    def get_queryset(self):
        qs = Listing.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(discription__icontains = query)
        return qs



class ListingPostApiView(generics.CreateAPIView):
    Permission_classes      = []
    authentication_classes  = []
    queryset                = Listing.objects.all()
    serializer_class        = ListingSerializer

class ListingGetApiView(generics.RetrieveAPIView):
    Permission_classes      = []
    authentication_classes  = []
    queryset                = Listing.objects.all()
    serializer_class        = ListingSerializer
    lookup_field            = 'id'


class ListingPutApiView(generics.UpdateAPIView):
    Permission_classes      = []
    authentication_classes  = []
    queryset                = Listing.objects.all()
    serializer_class        = ListingSerializer
    lookup_field            = 'id'


class ListingDeleteApiView(generics.DestroyAPIView):
    Permission_classes      = []
    authentication_classes  = []
    queryset                = Listing.objects.all()
    serializer_class        = ListingSerializer
    lookup_field            = 'id'
