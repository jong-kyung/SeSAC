from django.test import TestCase
from vote.models import Choice, Question
from django.urls import reverse
# Create your tests here.
class QuestionModelTests(TestCase):
    def test_question_views(self):
        response = self.client.get(reverse('question_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'quest.html')
    
    def test_choice_views(self):
        q = Question.objects.create(question = '오늘 밥 어디서 먹지?')
        Choice.objects.create(question = q, choice_text = '가화만사성',)

        choice = Choice.objects.get(question = q)

        response = self.client.get(reverse('choice_list', args=[q.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(q.question, '오늘 밥 어디서 먹지?')

        response = self.client.post(reverse('choice_list', args=[choice.pk]), {'choice': choice.pk}) # choice name값에 choice.pk 첨부
        self.assertEqual(response.status_code, 302)