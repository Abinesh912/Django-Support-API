import json
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from tickets.models import Ticket


class TicketAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="TestPass123!"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token.key
        )

    def test_health_check(self):
        response = self.client.get("/health/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)["status"], "ok")
    
    def test_create_ticket(self):
        data = {
            "title": "Test support ticket",
            "description": "Testing ticket creation",
            "status": "OPEN",
            "priority": "HIGH",
        }
        response = self.client.post("/api/tickets/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 1)

    def test_ticket_list_requires_authentication(self):
        self.client.credentials()
        response = self.client.get("/api/tickets/")
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    
    def test_list_tickets(self):
        data = {
            "title": "List test ticket",
            "description": "Testing ticket listing",
            "status": "OPEN",
            "priority": "MEDIUM",
        }

        self.client.post("/api/tickets/", data)
        response = self.client.get("/api/tickets/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_ticket(self):
        data = {
            "title": "Update test ticket",
            "description": "Testing ticket update",
            "status": "OPEN",
            "priority": "LOW",
        }

        create_response = self.client.post("/api/tickets/", data)
        ticket_id = create_response.data["id"]

        response = self.client.patch(
            f"/api/tickets/{ticket_id}/",
            {"status": "IN_PROGRESS"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "IN_PROGRESS")
