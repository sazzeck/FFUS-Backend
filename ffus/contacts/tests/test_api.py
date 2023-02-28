import json

from django.http import HttpResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

import ffus.contacts.tests.constants as const

from ..models import FeedbackModel
from ..serializers import FeedbackSerializer


class SetUpFeedbackTestCase:
    FIRSTNAMES: list[str] = [
        "Dima",
        "Vlad",
        "Olga",
    ]

    PHONES: list[str] = [
        "+380613284194",
        "0665123711",
        "0552131231",
    ]

    EXPECTED_PHONES: list[str] = [
        "+380613284194",
        "+380665123711",
        "+380552131231",
    ]

    def setUp(self) -> None:
        data: dict[str, str] = dict(zip(const.FIRSTNAMES, const.PHONES))
        for firstname, phone_number in data.items():
            FeedbackModel.objects.create(
                firstname=firstname, phone_number=phone_number
            )


class CreateFeedbackTestCase(SetUpFeedbackTestCase, APITestCase):
    URL: str = "contacts:feedbackmodel-list"

    def setUp(self) -> None:
        self.first_valid_feedback: dict[str, str] = {
            "firstname": "Oleg",
            "phone_number": "+380692914172",
        }
        self.second_valid_feedback: dict[str, str] = {
            "firstname": "Vlad",
            "phone_number": "+380652018522",
        }
        self.empty_firstname: dict[str, str] = {
            "firstname": "",
            "phone_number": "0611114172",
        }
        self.empty_phone_number: dict[str, str] = {
            "firstname": "Sasha",
            "phone_number": "",
        }

    def test_create_first_feedback(self) -> None:
        response: HttpResponse = self.client.post(
            reverse(self.URL),
            data=json.dumps(self.first_valid_feedback),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_second_feedback(self) -> None:
        response: HttpResponse = self.client.post(
            reverse(self.URL),
            data=json.dumps(self.second_valid_feedback),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_empty_firstname(self) -> None:
        response: HttpResponse = self.client.post(
            reverse(self.URL),
            data=json.dumps(self.empty_firstname),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_empty_phone_number(self) -> None:
        response: HttpResponse = self.client.post(
            reverse(self.URL),
            data=json.dumps(self.empty_phone_number),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_duplicate_phone_number(self) -> None:
        for _ in range(2):
            response: HttpResponse = self.client.post(
                reverse(self.URL),
                data=json.dumps(self.first_valid_feedback),
                content_type="application/json",
            )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetFeedbackTestCase(SetUpFeedbackTestCase, APITestCase):
    URL: str = "contacts:feedbackmodel-detail"

    def test_get_valid_feedback(self) -> None:
        response: HttpResponse = self.client.get(reverse(self.URL, args=[1]))
        obj: FeedbackModel = FeedbackModel.objects.get(id=1)
        serializer: FeedbackSerializer = FeedbackSerializer(obj)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_feedback(self) -> None:
        response: HttpResponse = self.client.get(reverse(self.URL, args=[11]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ListFeedbackTestCase(SetUpFeedbackTestCase, APITestCase):
    URL: str = "contacts:feedbackmodel-list"

    def test_get_feedbacks(self) -> None:
        response: HttpResponse = self.client.get(reverse(self.URL))
        obj: FeedbackModel = FeedbackModel.objects.all()
        serializer: FeedbackSerializer = FeedbackSerializer(obj, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
