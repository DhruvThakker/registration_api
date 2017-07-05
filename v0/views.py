from django.shortcuts import render

# Create your views here.
from models import AuthUser
from rest_framework import viewsets,permissions
from serializers import UserInfoSerializer,CreateUserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from oauth2_provider.ext.rest_framework.authentication import OAuth2Authentication
from rest_framework.throttling import UserRateThrottle

class UserThrottle(UserRateThrottle):

    rate = '40/minute'

    def allow_request(self, request, view):
        return super(UserThrottle, self).allow_request(request, view)


class UserViewSet(viewsets.ModelViewSet):
    """
    **Use Case**

        *Get a paginated list of users registered to the edX platform.

            The list can be filtered by user_id.

            Each page in the list can contain up to 10 users.

        *Register a new user to edX platform

            Currently only admin can use this command to register users to 
            this platform.
            Users are registered directly as active member and email id is not verified.But email ids are validated 

            Each request can register a single user.

            Required parameters are :
                * fullname
                * username (Must be unique Only Alphanumerics,(-),(_) allowed) 
                * password (Must not be same as username)
                * email (Must be unique)
                * city



    **Example Requests**

          GET /api/registration/v0/register/

          GET /api/registration/v0/register/{user_id}/

          POST /api/registration/v0/register/ 
            {   'fullname'  : '<fullname>'
                'username'  : '<username>'
                'email'     : '<email_id>'
                'password'  : '<password>'
                'city'      : '<city>'
            }

          ** Post Parameters ** 
            A POST request must have following prameters
            
            * fullname  : Fullname of the user as it appears on their certificate. 
            * username  : Username of the user to be registered.(Must be unique) 
            * email     : EmailId of the user to be registered.(Must be unique)
                          This will be used by the user for logging in to edX platform.
            * password  : Password for loging in to edX platform.
            * city      : City of which the user is a resident.

    **GET Response Values**
        On success with Response Code <200>

        * count: The number of Users registered in the edX platform.

        * next: The URI to the next page of courses.

        * previous: The URI to the previous page of courses.

        * num_pages: The number of pages listing courses.

        * results:
            A list of Users returned. Each collection in the list
            contains these fields.

            * id: The unique identifier for the user.

            * username: The username of the user.

            * email: The email id of the user


    **POST Response Value**

        On success with Response Code <200>

        Following details of successfully registered user are obtained

        * id  (Unique value assigned to the user.)
        * username
        * email 

    """

    http_method_names = ['get', 'post', 'head', 'put']
    authentication_classes = (SessionAuthentication, BasicAuthentication, OAuth2Authentication)
    permission_classes = (permissions.IsAdminUser,)
    queryset = AuthUser.objects.all()
    throttle_classes = (UserThrottle,)

    def get_serializer_class(self):

        if self.action == 'list':
            return UserInfoSerializer
        if self.action == 'create':
            return CreateUserSerializer
        return UserInfoSerializer
