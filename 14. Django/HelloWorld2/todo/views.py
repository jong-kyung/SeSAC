from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Todo

def todo_list(request):
    todo_list = Todo.objects.all()

    return render(request, 'list.html', {
        'todos': todo_list
    })

def todo_write(request):
    if request.method == 'POST':
        r_title = request.POST['title']
        r_content = request.POST['content']
        print(f'제목:{r_title}, 내용:{r_content}')

        Todo.objects.create(title=r_title, content=r_content)
        return redirect('todo_list')
    else:
        return render(request, 'write.html')


def todo_detail(request, pk):
    todo_detail = get_object_or_404(Todo, pk=pk)
    return render(request, 'detail.html', {
        'todo':todo_detail
    })

def update_todo(request, pk):
    todo_detail = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        r_title = request.POST['title']
        r_content = request.POST['content']
        print(f'수정할제목:{r_title}, 수정할내용:{r_content}')
        Todo.objects.update(title = r_title, content = r_content)
        return redirect('todo_list')
    else:
        return render(request, 'edit.html', {
            'todo':todo_detail
        })

def del_todo(request,pk):
    todo_detail = get_object_or_404(Todo, pk=pk)
    todo_detail.delete()
    return redirect('todo_list')