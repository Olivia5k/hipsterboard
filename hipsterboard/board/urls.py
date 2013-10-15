from django.conf.urls import patterns
from hipsterboard.board.views import BoardView

urlpatterns = patterns(
    '',
    (r'^$', BoardView.as_view()),
)
