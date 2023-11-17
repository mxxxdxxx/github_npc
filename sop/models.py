from django.db import models

# database 하나 = class
# Model을 잡는 것 = database table을 만드는 것
# models.Model 상속받아서 만듦
class Reporter(models.Model) :
    # 속성을 괄호 안에 넣어준다.
    full_name = models.CharField(max_length=30)
    
    # self가 들어감 -> instance가 생성돼야 호출
    def __str__(self) :
        return self.full_name
    
class Article(models.Model) :
    # auto_now_add=True (첫 발행 시간 고정)
    # auto_add=True (수정 시간 매번 업데이트)
    pub_date = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=200)
    content = models.TextField()
    # Reporter 객체를 참조함
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
    # self가 들어감 -> instance가 생성돼야 호출
    def __str__(self) :
        return self.headline
