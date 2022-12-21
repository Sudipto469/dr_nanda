from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..models import Product, Review, Hospital
# from ..serializer import ProductSerializer , HospitalSerializer
from ..serializers.hospitalSerializer import HospitalSerializer

@api_view(['GET'])
def getHospitals(request):
    hospital = Hospital.objects.all()
    # hospital = Hospital.
    serializer = HospitalSerializer(hospital, many=True)
    return Response(serializer.data)

# products = Product.objects.all()
#     serializer = ProductSerializer(products,many = True)
#     return Response(serializer.data)
