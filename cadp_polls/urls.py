from django.urls import path
from .views import (PollListView, PollDetailView,
                    VoteCreateView, VoteListView,
                    ExportPollResultsView, PollResultsView)


urlpatterns = [
    path('polls/', PollListView.as_view(), name='poll-list'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='poll-detail'),
    path('votes/', VoteCreateView.as_view(), name='vote-create'),
    path('votes/all/', VoteListView.as_view(), name='vote-list'),
    path('polls/export/', ExportPollResultsView.as_view(), name='export-poll-results'),
    path('polls/<int:poll_id>/results/', PollResultsView.as_view(), name='poll-results'),
]
