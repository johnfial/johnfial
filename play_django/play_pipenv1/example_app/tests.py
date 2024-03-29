# https://docs.djangoproject.com/en/3.2/intro/tutorial05/
import datetime
from django.http import response

from django.urls import reverse
from django.utils import timezone
from django.test import TestCase, testcases

from .models import Question

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase):    

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('example:index'))
        # may be error here for different app name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls here!")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
    
    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('example:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('example:index'))
        print(response.context)
        print(response.context.latest_question_list)
        self.assertContains(response, 'No polls here!') # this should be the same as the .html response!
        self.assertQuerysetEqual(response.content['latest_question_list'], [])
        
    def test_future_question_and_past_question(self):

        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        past_question = create_question(question_text='Future question.', days=-30)
        future_question = create_question(question_text="future question", days=30)
        response = self.client.get(reverse('example:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question])
        # merritt had [past_question] in the list above, django docs just have question

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past Question 1.", days=-30)
        question2 = create_question(question_text="Past question 2", days=-5)
        response = self.client.get(reverse('example:index'))
        self.assertQuerysetEqual(response.content['latest_question_list'], [question2, question1])

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse('example:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_questions(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past question.", days=-5)
        url = reverse('example:detail', args=(past_question.id,))
        response = self.client.get(url)
        # print('^^^^ ' * 500)
        self.assertContains(response, past_question.question_text)
