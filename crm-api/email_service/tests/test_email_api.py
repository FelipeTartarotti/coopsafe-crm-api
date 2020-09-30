from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

EMAIL_URL = reverse('api:email_service:send-list')

class PublicRecipeApiTests(TestCase):
    """Test unauthenticated recipe API access"""

    def setUp(self):
        self.client = APIClient()

    def test_email_send(self):
        """Testa o envio de email"""

        payload = {
            "emails":[
                "tartarotti.felipe@gmail.com"
            ],
            "body":"<strong>TESTE</strong>",
            "subject":"Assunto do email",
            "from_email":"nao-responda@mutualtech.com.br",
            "use_tls":"True",
            "host":"mail.mutualtech.com.br",
            "username":"nao-responda@mutualtech.com.br",
            "password":"46ty98iu@",
            "port":587
        }

        res = self.client.post(EMAIL_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)