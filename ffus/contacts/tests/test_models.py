from django.test import TestCase

import ffus.contacts.tests.constants as const

from ..models import FeedbackModel


class FeedbackModelTestCase(TestCase):
    def setUp(self) -> None:
        data: dict[str, str] = dict(zip(const.FIRSTNAMES, const.PHONES))
        for firstname, phone_number in data.items():
            FeedbackModel.objects.create(
                firstname=firstname, phone_number=phone_number
            )

    def test_get_feedback(self) -> None:
        expected_data: dict[str, str] = dict(
            zip(const.FIRSTNAMES, const.EXPECTED_PHONES)
        )
        for firstname, phone_number in expected_data.items():
            obj: FeedbackModel = FeedbackModel.objects.get(firstname=firstname)
            self.assertEqual(obj.get_feedback(), f"{firstname}: {phone_number}")
