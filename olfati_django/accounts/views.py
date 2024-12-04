import codecs
from random import randint
from sqlite3 import IntegrityError
from django.contrib.auth.models import Group

from kavenegar import KavenegarAPI
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .models import OtpModel, UserModel
from .serializer import OtpSerializers, UserSerializers


class UserView(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            if UserModel.objects.filter(phone_number=phone_number).exists():
                return Response({'error': 'Repetitious Number'}, status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    user_instance = serializer.save(is_active=True)
                    refresh = RefreshToken.for_user(user_instance)
                    token = {'refresh': str(refresh), 'access': str(
                        refresh.access_token)}
                    response_data = {
                        'message': 'Compiled Profile Successfully',
                        'user': serializer.data,
                        'token': token
                    }
                    return Response(response_data, status.HTTP_201_CREATED)
                except IntegrityError:
                    return Response({'error': 'Unknown Error'}, status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        userData = UserModel.objects.all()
        srz = UserSerializers(instance=userData, many=True)
        return Response(srz.data)


class Helper:
    @staticmethod
    def generate_otp_code():
        return str(randint(1000, 9999))


class SendCode(APIView):
    def post(self, request):
        phone_number = request.data.get("phone_number")
        if not phone_number:
            return Response({'status': status.HTTP_400_BAD_REQUEST, 'message': 'Invalid phone number.'})
        try:
            code = Helper.generate_otp_code()
            api_key = '366A34417873646451665051752B6B4A4F784B77484E50344B68374434346E53684F387558346D717349773D'
            params = {
                    'receptor': phone_number,
                    'template': 'verify',
                    'token': code,
                    'type': 'sms',  # sms vs call
                }
            api = KavenegarAPI(api_key)  
            api.verify_lookup(params)
            OtpModel.objects.create(phone_number=phone_number, otpCode=code)
            return Response({'message': 'Code Sent!'}, status.HTTP_200_OK)
        except Exception as e:
            error_message = str(e)
            decoded_error_message = codecs.decode(
                error_message, 'unicode-escape').encode('latin-1').decode('utf-8')
            return Response({'message': error_message}, status.HTTP_500_INTERNAL_SERVER_ERROR)


class VerifyOTPView(APIView):
    def post(self, request):
        serializer = OtpSerializers(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            code = serializer.validated_data['otpCode']
            try:
                otp_code = OtpModel.objects.get(
                    phone_number=phone_number, otpCode=code)
                try:
                    user = UserModel.objects.get(
                        phone_number=phone_number, is_active=True)
                    userSRZ = UserSerializers(instance=user).data
                    refresh = RefreshToken.for_user(user)
                    token = {'refresh': str(refresh), 'access': str(
                        refresh.access_token)}
                    otp_code.delete()
                    return Response({'is_active': True, 'user': userSRZ, 'token': token}, status.HTTP_200_OK)
                except UserModel.DoesNotExist:
                    return Response({'is_active': False}, status.HTTP_200_OK)
            except OtpModel.DoesNotExist:
                return Response({'message': 'OTP code not valid'}, status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': serializer.errors}, status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdminLoginView(APIView):
  #  permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
       # password = request.data.get('password')
        user = authenticate(username=username)
        if user is not None and user.is_superuser:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid Credentials or Not Superuser'}, status=status.HTTP_401_UNAUTHORIZED)

class ResetPasswordView(APIView):
    def post(self, request):
        username = request.data.get('username')
        new_password = request.data.get('new_password')
        try:
            user = UserModel.objects.get(username=username)
            user.set_password(new_password)
            user.save()

            # اضافه کردن کاربر به گروه مورد نظر (مثلاً گروه staff)
            staff_group = Group.objects.get(name='teacher')  # فرضاً که گروهی به نام staff وجود دارد
            user.groups.add(staff_group)

            return Response({'message': 'Password reset successfully. User now has access to admin panel.'})
        except UserModel.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
class EditProfileView(APIView):
 def post(self, request):
       # if not request.user.is_superuser:
        #    return Response({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
        
        username = request.data.get('username')
        new_username = request.data.get('new_username', None)
        first_name = request.data.get('first_name', None)
        last_name = request.data.get('last_name', None)
        study_field = request.data.get('study_field', None)
        melli_code = request.data.get('melli_code', None)
        phone_number = request.data.get('phone_number', None)
        try:
            user = UserModel.objects.get(username=username)
            if new_username:
                user.username = new_username
            if last_name:
                user.last_name = last_name
            if first_name:
                user.first_name = first_name
            if study_field:
                user.study_field = study_field
            if melli_code:
                user.melli_code = melli_code
            if phone_number:
                user.phone_number = phone_number
            user.save()
            # سریالایز و برگرداندن داده‌های کاربر
            user_data = UserSerializers(user).data
            return Response({'message': 'Profile updated successfully', 'data': user_data})
        except UserModel.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)
