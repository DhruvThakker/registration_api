from rest_framework import serializers
from models import AuthUser,AuthUserprofile

class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('url', 'id', 'username','email', 'date_joined')

class CreateUserSerializer(serializers.ModelSerializer):

    city = serializers.CharField(write_only= True)
    fullname = serializers.CharField(write_only= True)
    class Meta:
        model = AuthUser
        fields = ('id','fullname','username','email','password','city')
        extra_kwargs = {'password': {'write_only': True, 'style':{'input_type':'password'}},'id':{'read_only':True}}

    def validate(self, data):
        import re
        pattern = re.compile(r'[A-Za-z0-9_-]+$')
        if not pattern.match(data['username']):
            raise serializers.ValidationError('Username can only have alphanumerics,(-),(_)')

        pattern1 = re.compile(r'[A-Za-z0-9_-][A-Za-z0-9 _-]*$')
        if not pattern1.match(data['fullname']):
            raise serializers.ValidationError('Fullname can only have alphanumerics,(-),(_),(<blank space>) '
                                              'and cannot start with blank space')

        if not pattern1.match(data['city']):
            raise serializers.ValidationError('City can only have alphanumerics,(-),(_),(<blank space>) '
                                              'and cannot start with blank space')

        if data['username']==data['password']:
            raise serializers.ValidationError('Username Cannot be same as password')
	
	pattern2 = re.compile(r'[^@]+@[^@]+\.[^@]+')
        if not pattern2.match(data['email']):
            raise serializers.ValidationError('Invalid Email Id')

        return  data
    def create(self, validated_data):
        user = AuthUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        profile = AuthUserprofile.create(validated_data['fullname'],user,validated_data['city'])
        profile.save()
        return user
