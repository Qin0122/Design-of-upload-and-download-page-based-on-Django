from rest_framework import serializers


class FileSerializer(serializers.Serializer):
    filename = serializers.CharField(label='文件名', max_length=100)
