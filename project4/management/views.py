import requests
from django.utils import timezone
from scheduler.models import Schedule
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import Memo


class PostUpdate(UpdateView):
    model = Memo  # 모델은 Memo
    fields = ['content']  # 수정할 필드는 content
    template_name = 'management/edit.html'  # 사용할 템플릿 파일

    success_url = reverse_lazy('management:management')  # 수정 후 리다이렉트할 URL

    def get_object(self):
        """ 수정할 Memo 객체를 가져오는 메서드 """
        return Memo.objects.first()  # 첫 번째 Memo 객체 (하나만 존재한다고 가정)


def weather_warning(request):
    if not request.user.is_authenticated:
        # 로그인하지 않은 사용자가 접근하면 이전 페이지로 리디렉션
        referer = request.META.get('HTTP_REFERER', '/')  # 이전 페이지 URL을 가져옴
        return redirect(referer)
    # 기상 특보가 있는 URL
    URL = "https://www.weatheri.co.kr/forecast/forecast01.php?rid=0801030101&k=6&a_name=%EC%A0%84%EC%A3%BC"

    # 요청 보내기
    res = requests.get(URL)

    # 응답이 성공적이면, HTML을 파싱하여 기상 특보 내용 추출
    if res.status_code == 200:
        res.encoding = "UTF-8"

        # 기상 특보 내용 추출 (marquee 태그 내 텍스트)
        start_index = res.text.find('<marquee direction="left"')
        end_index = res.text.find('</marquee>', start_index)

        if start_index != -1 and end_index != -1:
            # 특보 내용 추출
            weather_alert = res.text[start_index:end_index]
            weather_alert = weather_alert.split(">")[1].split("<")[0].strip()  # ">" 이후, "<" 이전 텍스트 추출

        memo = Memo.objects.first()

        today = timezone.now().date()

        camera_stream = "http://113.198.63.27:20750/monitor"

        # 오늘 일정만 필터링 (start_time이 오늘인 일정)
        schedules = Schedule.objects.filter(start_time__date=today)
        filename = './people.csv'

        with open(filename, encoding="utf-8-sig") as f:

            alarm = ''
            lines = f.readlines()
            for line in lines[0:2]:
                alarm += (str(line.split("/")[1]) + '<br>')


    return render(
        request,
        'management/index.html',
        {'camera_stream': camera_stream, 'weather_alert': weather_alert, 'memo': memo, 'schedules': schedules,
         'alarm': alarm, })
