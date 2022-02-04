from rest_framework.response import Response
from rest_framework.decorators import api_view


#views goes here

@api_view(['GET'])
def getData(request):
    person = {'name': 'victor', 'age': 22}
    return Response(person)


