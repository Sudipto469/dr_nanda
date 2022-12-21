from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..models import Product, Review, Hospital, Clinic
# from ..serializer import ProductSerializer , HospitalSerializer
from ..serializers.clinicSerializer import ClinicSerializer

@api_view(['GET'])
def getClinics(request):
    clinic = Clinic.objects.all()
    # hospital = Hospital.
    serializer = ClinicSerializer(clinic, many=True)
    return Response(serializer.data)
