from rest_framework import serializers
from main.models import Proxy, UserInfo, Classify, Article, CommentInfo


class UserInfoSerializer(serializers.ModelSerializer):
    format_create_time = serializers.SerializerMethodField(method_name='get_format_create_time')
    format_update_time = serializers.SerializerMethodField(method_name='get_format_update_time')

    @staticmethod
    def get_format_create_time(obj):
        return obj.create_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_format_update_time(obj):
        return obj.update_time.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        model = UserInfo
        fields = ['name', 'phone', 'email', 'gender', 'face_info', 'picture', 'password', 'create_time', 'update_time',\
                  'is_delete', 'format_create_time', 'format_update_time']


class ClassifySerializer(serializers.ModelSerializer):
    format_create_time = serializers.SerializerMethodField(method_name='get_format_create_time')
    format_update_time = serializers.SerializerMethodField(method_name='get_format_update_time')

    @staticmethod
    def get_format_create_time(obj):
        return obj.create_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_format_update_time(obj):
        return obj.update_time.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Classify
        fields = ['name', 'create_time', 'update_time', 'comment', 'is_delete', 'format_create_time',\
                  'format_update_time']


class ArticleSerializer(serializers.ModelSerializer):
    format_create_time = serializers.SerializerMethodField(method_name='get_format_create_time')
    format_update_time = serializers.SerializerMethodField(method_name='get_format_update_time')
    user_id = serializers.SerializerMethodField(method_name='get_user_id')
    user_name = serializers.SerializerMethodField(method_name='get_user_name')
    classify_id = serializers.SerializerMethodField(method_name='get_classify_id')
    classify_name = serializers.SerializerMethodField(method_name='get_classify_name')

    @staticmethod
    def get_format_create_time(obj):
        return obj.create_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_format_update_time(obj):
        return obj.update_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_user_id(obj):
        return obj.user_info.id

    @staticmethod
    def get_user_name(obj):
        return obj.user_info.name

    @staticmethod
    def get_classify_id(obj):
        return obj.classify.id

    @staticmethod
    def get_classify_name(obj):
        return obj.classify.name

    class Meta:
        model = Article
        fields = ['title', 'picture', 'content', 'create_time', 'update_time', 'is_delete', 'format_create_time',\
                  'format_update_time', 'user_id', 'user_name', 'classify_id', 'classify_name']


class CommentInfoSerializer(serializers.ModelSerializer):
    format_create_time = serializers.SerializerMethodField(method_name='get_format_create_time')
    format_update_time = serializers.SerializerMethodField(method_name='get_format_update_time')
    user_id = serializers.SerializerMethodField(method_name='get_user_id')
    user_name = serializers.SerializerMethodField(method_name='get_user_name')
    article_id = serializers.SerializerMethodField(method_name='get_article_id')
    article_title = serializers.SerializerMethodField(method_name='get_article_title')

    @staticmethod
    def get_format_create_time(obj):
        return obj.create_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_format_update_time(obj):
        return obj.update_time.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_user_id(obj):
        return obj.user_info.id

    @staticmethod
    def get_user_name(obj):
        return obj.user_info.name

    @staticmethod
    def get_article_id(obj):
        return obj.article.id

    @staticmethod
    def get_article_title(obj):
        return obj.article.title

    class Meta:
        model = CommentInfo
        fields = ['content', 'create_time', 'update_time', 'is_delete', 'format_create_time', 'format_update_time',\
                  'user_id', 'user_name', 'article_id', 'article_title']


class ProxySerializer(serializers.ModelSerializer):
    format_time = serializers.SerializerMethodField(method_name='get_format_time')

    @staticmethod
    def get_format_time(obj):
        return obj.last_validation_time.strftime("%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Proxy
        fields = ['ip', 'port', 'anonymous', 'type', 'location', 'response_speed', 'last_validation_time', 'score',\
                  'is_delete', 'format_time']