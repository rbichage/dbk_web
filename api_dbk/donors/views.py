from rest_framework import permissions, status
from rest_framework.compat import authenticate
from rest_framework.compat import authenticate
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from accounts.models import Donor
from api_dbk.donors.donor_serializers import SignUpSerializer, PasswordSerializer
from . import donor_serializers as sz


class SignUpView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    @parser_classes((JSONParser, FormParser, MultiPartParser))
    def post(request, format=None):
        try:
            serializer = SignUpSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

                response = Response({
                    "success": True,
                    "message": "Registration successful",
                    "donor": serializer.data,
                })

                return response

            # else:
            #     response = Response({
            #         "success": False,
            #         "message": serializer.errors,
            #
            #     }, 406)

            if Donor.objects.filter(username=request.data.get("username")).exists():
                response = Response({
                    "success": False,
                    "message": "This username is already in use",

                }, 400)

                response.reason_phrase = "username already in use"
                return response

            if Donor.objects.filter(email=request.data.get("email")).exists():
                response = Response({
                    "success": False,
                    "message": "This email is already in use",

                }, 406)

                response.reason_phrase = "this email is already taken"
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
                    {

                        "message": "Incorrect password, please try again.",
                        "success": False
                    }, status=HTTP_400_BAD_REQUEST)

            else:
                response = Response(
                    {
                        "message": "Kindly check your username",
                        "success": False
                    }, status=HTTP_400_BAD_REQUEST)

            return response

        donor = Donor.objects.get(username=username)

        serializer = sz.DonorLoginSerializer(donor, many=False)
        response = Response(
            {
                "success": True,
                "message": "login successful",
                "donor": serializer.data})

        return response
    except Exception as e:
        return Response({"success": False, "message": str(e)})


class UpdatePassword(GenericAPIView):
    """
    An endpoint for changing password.
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = PasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
