from django.contrib import admin
from .models import Memo  # Memo 모델을 import합니다.

# Memo 모델을 Django Admin에 등록
admin.site.register(Memo)

