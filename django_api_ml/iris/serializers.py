from rest_framework import serializers

class iris_serializer(serializers.Serializer):
  
    a = serializers.IntegerField(required=True,label='a')
    b = serializers.IntegerField(required=True,label='b')
    c = serializers.IntegerField(required=True,label='c')
    d = serializers.IntegerField(required=True,label='d')
    class Meta:
        fields = '__all__'