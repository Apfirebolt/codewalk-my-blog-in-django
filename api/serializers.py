from rest_framework import serializers
from users.models import CustomUser
from blog.models import Category, Post, PostImages, Tag, PostTag, About, Experience
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': ('No account exists with these credentials, check password and email')
    }

    def validate(self, attrs):
        
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data 
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['id'] = self.user.id
        data['is_admin'] = self.user.is_superuser
        return data


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text='Leave empty if no change needed',
        min_length=8,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    access = serializers.SerializerMethodField()
    refresh = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'id', 'is_staff', 'password', 'access', 'refresh',)
    
    def get_refresh(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh)

    def get_access(self, user):
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token),
        return access

    def create(self, validated_data):
        user = super(CustomUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class ListCustomUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'id', 'is_staff')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    
    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Category name must be at least 3 characters long')
        nameExists = Category.objects.filter(name=value)
        if nameExists:
            raise serializers.ValidationError('Category with this name already exists')
        return value
    

class AboutSerializer(serializers.ModelSerializer):
    author_email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = About
        fields = '__all__'
        read_only_fields = ['author']

    def create(self, validated_data):
        # Get the user from the context
        author = self.context['request'].user
        about = About.objects.create(author=author, **validated_data)
        return about


    def get_author_email(self, obj):
        return obj.author.email
    

class ExperienceSerializer(serializers.ModelSerializer):
    author_email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ['author']

    def create(self, validated_data):
        # Get the user from the context
        author = self.context['request'].user
        experience = Experience.objects.create(author=author, **validated_data)
        return experience

    def get_author_email(self, obj):
        return obj.author.email


class ListPostsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']