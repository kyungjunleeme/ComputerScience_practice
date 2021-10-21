from django.db import models

# Create your models here.

# https://hyunalee.tistory.com/37
class Minute(models.Model):
    class OpenChoices(models.TextChoices):
        # 팀확인되는 대로 추가 가능함
        nonopen = "0", "비공개"
        open = "1", "공개"
        member = "2", "회의 참석자"
        operation_team = "team1", "경영지원팀"
        it_team = "team2", "it지원팀"

    meeting = models.ForeignKey("meeting.Meeting", on_delete=models.CASCADE)  # 회의
    title = models.CharField(max_length=50)  # 회의록 제목
    content = models.TextField()  # 회의록 내용
    path = models.FileField(
        null=True, blank=True
    )  # 첨부파일 경로/media/2021-10-11/ upload_to 미지정시에는 기본설정된 곳
    type = models.CharField(
        max_length=20, choices=OpenChoices.choices, null=True, blank=True
    )
    # __str__ returned non-string (type int)

    def __str__(self):
        return str(self.pk)
