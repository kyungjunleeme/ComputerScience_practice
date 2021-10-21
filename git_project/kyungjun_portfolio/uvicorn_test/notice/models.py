from django.db import models

# Create your models here.


class Notice(models.Model):
    host = models.CharField(max_length=50)  # 작성한 사람
    # 토큰 값 활용해서 -> user 복원하고 -> user table내에서 작성권한 있는지 확인 하면 됨
    title = models.CharField(max_length=50)
    content = models.TextField()
