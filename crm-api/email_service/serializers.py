from rest_framework import serializers

class EmailServiceSerializer(serializers.Serializer):

    emails = serializers.ListField(child=serializers.CharField())
    use_tls = serializers.BooleanField()
    host = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField()
    port = serializers.CharField()
    from_email = serializers.CharField()
    subject = serializers.CharField()
    body = serializers.CharField()








