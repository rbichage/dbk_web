from django.shortcuts import get_object_or_404
from django.views import generic
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.compat import authenticate
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from accounts.models import Donor
from api_dbk.donors.donor_serializers import SignUpSerializer, DonorProfileSerializer
from . import donor_serializers as sz


class SignUpView(APIView):
    permission_classes = (IsAuthenticated, )

    @staticmethod
    @parser_classes((JSONParser, FormParser, MultiPartParser))
    def post(request, format=None):
        try:
            serializer = SignUpSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                response = Response({
                    "success": True,
                    "donor": serializer.data,
                })

                return response

            else:
                response = Response({
                    "success": False,
                    "error": serializer.errors,

                }, status=406)

                if Donor.objects.filter(username=request.data.get("username")).exists():
                    response.reason_phrase = "username already in use"

                if Donor.objects.filter(email=request.data.get("email")).exists():

                    response.reason_phrase = "this email is already taken"
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
@permission_classes((IsAuthenticated,))
@parser_classes((JSONParser, FormParser, MultiPartParser))
def login(request):
    # serializer = sz.LoginSerializer(
    #     data=request.data, context={'request': request}
    # )
    # if not serializer.is_valid():
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # user = get_object_or_404(Donor, username=serializer.validated_data['username'])
    # if not user.check_password(serializer.validated_data['password']):
    #     return Response({'error': 'Incorrect username or password'}, status=status.HTTP_400_BAD_REQUEST)
    # serializer = sz.DonorLoginSerializer(user)
    # return Response(serializer.data)

    try:

        username = request.data.get("username")
        password = request.data.get("password")

        donor = authenticate(request, username=username, password=password)
        if not donor:

            if Donor.objects.filter(username=username).exists():
                response = Response(
                    {"message": "incorrect password, please try again.", }, status=HTTP_400_BAD_REQUEST)

            else:
                response = Response(
                    {"message": "please check your username"}, status=HTTP_400_BAD_REQUEST)

            return response

        donor = Donor.objects.get(username=username)

        serializer = sz.DonorLoginSerializer(donor, many=False)
        response = Response(
            {"message": "login successful",
             "donor": serializer.data})
        response.reason_phrase = "Hello " + donor.username

        return response
    except Exception as e:
        return Response({"success": False, "message": str(e)})
