from django.db import models
from django.conf import settings

# Create your models here.


class Room(models.Model):
    company_type = models.CharField(max_length=100)  # 회의실 지점
    name = models.CharField(max_length=100)  # 회의실 이름
    people_type = models.IntegerField()  # 회의실 이용 type
    location = models.CharField(max_length=100)  # 회의실 위치

    def __str__(self):
        return str(self.pk)


class Meeting(models.Model):
    host = models.CharField(max_length=50)  # null=False, blank=False, 필수 값
    # token 값 활용해서-> 변환해서 저장 ## 창성님이 알려주신 방법대로
    # 1) https://han-py.tistory.com/353 , #2) request.user # 요지는 forntend, 자동적으로 값 가져오도록
    title = models.CharField(max_length=100)
    meeting_date = models.DateField()
    room_set = models.ManyToManyField(Room)  # 선택한 회의실
    user_set = models.ManyToManyField(settings.AUTH_USER_MODEL)  # 회의 참석자들 [1, 2, 3]
    meeting_starttime = models.DateTimeField()  # 14:00
    meeting_end_time = models.DateTimeField()  # 10:00

    def __str__(self):
        return str(self.pk)
