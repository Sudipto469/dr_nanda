from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..models import Product, Review, Hospital, Lab
# from ..serializer import ProductSerializer , HospitalSerializer
from ..serializers.labSerialier import LabSerializer

@api_view(['GET'])
def getLabs(request):
    lab = Lab.objects.all()
    # hospital = Hospital.
    serializer = LabSerializer(lab, many=True)
    return Response(serializer.data)
