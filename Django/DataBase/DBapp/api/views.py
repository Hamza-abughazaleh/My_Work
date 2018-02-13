from rest_framework.generics import CreateAPIView,ListAPIView , RetrieveAPIView , DestroyAPIView , UpdateAPIView
from DBapp.models import Trip , AuthUser
from DBapp.api.serializers import TripListSerializer,TripDetailSerializer,TripCreateSerializer,AuthUserSerializer

class TripCreateAPIView(CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripCreateSerializer

    def perform_create(self, serializer):
        userid = AuthUser.objects.get(id=self.request.user.id)
        serializer.save(user=userid)

class TripListAPIView(ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripListSerializer

class TripDetailAPIView(RetrieveAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripDetailSerializer

class TripUpdateAPIView(UpdateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripDetailSerializer

class TripDeleteAPIView(DestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripDetailSerializer
