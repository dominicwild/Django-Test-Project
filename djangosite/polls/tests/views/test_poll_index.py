import datetime
from django.test import TestCase

from django.urls import reverse
from django.utils import timezone

from polls.models.question import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):

    def test_no_questions_stored_show_no_questions(self):
        response = self.get_index_page()
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question_is_displayed(self):
        question = create_question(question_text="Past question.", days=-30)
        response = self.get_index_page()
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question_is_not_displayed(self):
        create_question(question_text="Future question.", days=30)
        response = self.get_index_page()
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question_only_past_question_displayed(self):
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.get_index_page()
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_questions_are_displayed(self):
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.get_index_page()
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )

    def get_index_page(self):
        return self.client.get(reverse('polls:index'))