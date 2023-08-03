from django.shortcuts import render, get_object_or_404, redirect
from vote.models import Question, Choice
# Create your views here.
def question_list(request):
    question = Question.objects.all()
    return render(request, 'quest.html', {
            'questions':question
        })

def choice_list(request, pk):
    question = get_object_or_404(Question, pk=pk)
    if request.method == 'POST':
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_choice.count += 1
        selected_choice.save()

        return redirect('question_list')
    else:
        selected_choice = question.choice_set.all()
        print(selected_choice)
        return render(request, 'choice.html', {'questions':selected_choice})