import json
from rest_framework import viewsets, mixins, status
from django.http import HttpResponse
from django.utils.html import strip_tags
from rest_framework import viewsets
from rest_framework.decorators import action, authentication_classes, permission_classes
from rest_framework.response import Response
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
from django.core.mail import EmailMultiAlternatives
from email_service.serializers import EmailServiceSerializer


@authentication_classes([])
@permission_classes([])
class EmailServiceViewSet(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        "Envia e-mails em massa"
        serializer = EmailServiceSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            try:
                striped_body = strip_tags(validated_data["body"])
                connection = get_connection(host=validated_data["host"],
                                            port=validated_data["port"],
                                            username=validated_data["username"],
                                            password=validated_data["password"],
                                            use_tls=validated_data["use_tls"])

                msg = EmailMultiAlternatives(
                    validated_data["subject"],
                    striped_body,
                    validated_data["from_email"],
                    validated_data["emails"],
                    connection=connection
                )

                msg.attach_alternative(validated_data["body"], "text/html")
                msg.send(fail_silently=False)

                return Response("E-mail enviado com sucesso")

            except Exception as error:
                smtp_error = "Erro ao enviar e-mail"

                try:
                    if error.smtp_error:
                        smtp_error = error.smtp_error.decode("utf-8")
                except:
                    pass

                try:
                    if error.strerror:
                        smtp_error = error.strerror
                except:
                    pass

                return HttpResponse(smtp_error, status=400)

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


