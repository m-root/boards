from django.shortcuts import render
from django.http import HttpResponse, Http404
from boards.models import Board, Topic, Post
from django.shortcuts import redirect,render, get_object_or_404
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    # return HttpResponse('Hello World')
    boards = Board.objects.all()
    boards_list = list()

    # for board in boards:
    #     boards_names.append(board.name)
    #
    # response_html = '<br>'.join(boards_names)
    #
    # return HttpResponse(response_html)
    return render(request, 'home.html',{'boards':boards_list})





def board_topics(request, pk):
    # try:
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    # return render(request, 'topics.html', {'board':board})

    board_topics = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board_name':board_topics})

def new_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    # return render(request, 'new_topic.html', {'board':board})

    if request.method =='POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first() # TODO: get the current user logged in first

        topic = Topic.objects.create(
            subject=subject,
            board_name=board,
            starter=user
        )

        post = Post.objects.create(
            message = message,
            topic = topic,
            created_by=user
        )

        return redirect('board_topics', pk=board.pk) #TODO: redirect to the created page
    return render(request, 'new_topic.html', {'board':board})

