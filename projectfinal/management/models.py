from django.db import models


class Memo(models.Model):
    content = models.TextField()  # 메모의 내용을 저장하는 필드

    def __str__(self):
        return self.content[:50]