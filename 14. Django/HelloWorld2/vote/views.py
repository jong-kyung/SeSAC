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
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # question, choice join문법, choice의 fk와 question의 pk가 일치하는 값
        selected_choice.count += 1
        selected_choice.save()
        print(f'선택지:{selected_choice.Question.pk}')
        return redirect('result_choice', selected_choice.Question.pk)
    else:
        selected_choice = question.choice_set.all()
        return render(request, 'choice.html', {'questions':selected_choice})
    
def result_choice(request, pk):
    choice = Choice.objects.filter(Question = pk).all()
    print(choice)

    return render(request, 'result.html', {
        'choices' : choice
    })