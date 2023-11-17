from django.shortcuts import render
from .models import Article

# FBV : 함수 기반 Views
# request(url 객체)를 받는다.
# object : 각 DB 테이블을 관리하는 관리자 -> 얘를 호출해서 사용
# pub_data__year : pub_data의 속성 중 year를 가져올 때 __(더블언더바 사용)
# pub_data__year=year : equals 뒤의 year는 매개변수
# context : 페이지에 들어갈 콘텐츠들
# render 함수 : 순수 html, css, javascript를 클라이언트로 반환
# CRUD를 View 함수에서 진행한다.
def year_archive(request, year):
    year_article_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': year_article_list}
    return render(
        request,
        'sop/year_archive.html',
        context,
    )

def month_archive(request, year, month):
    month_article_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year':year, 'month':month, 'article_list': month_article_list}
    return render(
        request,
        'sop/month_archive.html',
        context,
    )

def article_detail(request, year, month, day):
    detail_article_list = Article.objects.filter(pub_date__year=year, pub_date__month=month, pub_date__day=day)
    context = {'year':year, 'month':month, 'day':day, 'article_list':detail_article_list}
    return render(
        request,
        'sop/article_detail.html',
        context,
    )