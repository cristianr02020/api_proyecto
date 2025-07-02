from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class TareaTests(APITestCase):

    def setUp(self):
        # Crear un usuario de prueba
        self.usuario = User.objects.create_user(username='testuser', password='testpass')
        self.url = '/api/tareas/'

        # Obtener token JWT
        refresh = RefreshToken.for_user(self.usuario)
        self.token = str(refresh.access_token)

        # Datos de tarea
        self.datos_tarea = {
            "titulo": "Prueba con usuario autenticado",
            "descripcion": "Creación desde test",
            "completada": False
        }

    def test_usuario_autenticado_puede_crear_tarea(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post(self.url, self.datos_tarea, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_usuario_no_autenticado_no_puede_crear_tarea(self):
        response = self.client.post(self.url, self.datos_tarea, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
