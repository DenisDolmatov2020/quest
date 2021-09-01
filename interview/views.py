import datetime
from rest_framework.generics import ListAPIView
from interview.models import Interview
from interview.serializers import InterviewSerializer


class InterviewList(ListAPIView):
    serializer_class = InterviewSerializer
    queryset = Interview.objects.filter(date_start__lte=datetime.date.today(), date_end__gte=datetime.date.today())
