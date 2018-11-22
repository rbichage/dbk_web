from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Donor
from api_dbk.donors.donor_serializers import SignUpSerializer
from . import donor_serializers as sz


class SignUpView(APIView):
    permission_classes = ()

    @staticmethod
    def post(request, format=None):
        try:
            serializer = SignUpSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                # token, created = Token.objects.get_or_create(user=serializer.instance)

                response = Response({
                    "user": serializer.data,
                    # "token": token.key
                })

                response.reason_phrase = "Welcome to dbk"
                return response
            else:
                response = Response({
                    "error": serializer.errors,
                    "error_": serializer.error_messages,
                    "data": request.data
                }, status=406)

                if Donor.objects.filter(username=request.data.get("username")).exists():
                    response.reason_phrase = "username already in use"
                else:
                    response.reason_phrase = "Failed to sign you up, Please contact admin"

                return response

        except Exception as e:
            response = Response({
                "message": "something went wrong on server",
                "success": False,
                "exception": str(e),
            }, 406)

            response.reason_phrase = str(e)
            return response


@api_view(["POST"])
@permission_classes((AllowAny,))
@parser_classes((JSONParser, FormParser, MultiPartParser))
def login(request):
    serializer = sz.LoginSerializer(
        data=request.data, context={'request': request}
    )
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user = get_object_or_404(Donor, username=serializer.validated_data['username'])
    if not user.check_password(serializer.validated_data['password']):
        return Response({'error': 'Incorrect username or password'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = sz.DonorLoginSerializer(user)
    return Response(serializer.data)












    # try:
    #
    #     username = request.data.get("username")
    #     password = request.data.get("password")
    #
    #     donor = authenticate(request, username=username, password=password)
    #     if not donor:
    #         response = Response({"message": "Invalid login credentials"}, status=HTTP_401_UNAUTHORIZED)
    #
    #         if Donor.objects.filter(username=username).exists():
    #             response.reason_phrase = "Wrong password"
    #         else:
    #             response.reason_phrase = "You don't have an account yet, Please create one"
    #
    #         return response
    #
    #     token, _ = Token.objects.get_or_create(user=donor)
    #     donor = Donor.objects.get(username=username)
    #
    #     serializer = DonorProfileSerializer(donor, many=False)
    #     response = Response(
    #         {"token": token.key,
    #          "user": serializer.data})
    #     response.reason_phrase = "Hello " + donor.first_name + ", Welcome"
    #
    #     return response
    # except Exception as e:
    #     return Response({"success": False, "message": str(e)})



























