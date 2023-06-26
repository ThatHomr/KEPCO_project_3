from django.db import models, migrations
from django.utils import timezone
from django import forms
# - DB에서 varchar2 또는 char 등 문자열 타입
from django.db.models.fields import CharField
# - DB에서 숫자형 타입 자동증가
from django.db.models.fields import AutoField
# - DB에서 number 또는 integer 등 숫자형 타입
from django.db.models.fields import IntegerField
# - DB에서 날짜와 시간을 갖는 필드.
# 날짜만 가질 경우는 DateField, 시간만 가질 경우는 TimeField를 사용한다.
from django.db.models.fields import DateTimeField
# - DB에서 대용량 문자열을 갖는 필드
from django.db.models.fields import TextField
# - DB에서 파일 업로드 필드

# - user 확장
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class User(AbstractUser):
    username = CharField(primary_key=True, max_length=20)
    password = CharField(max_length=20)
    email = CharField(max_length=100)
    phon = CharField(max_length=100)
    nickname = CharField(max_length=100)

    class Meta:
        # 실제 사용할 테이블 이름 정의
        db_table = "User"

        # 사용할 앱 이름 정의
        app_label = "mainapp"

        # 외부 데이터베이스에 테이블 존재여부 확인
        # - 존재하면 : False
        # - 존재하지 않으면 : True
        # --> 일반적으로 외부에 테이블을 생성한 후 개발이 진행됨
        managed = False

class Category(models.Model):
    cate_num = IntegerField(primary_key=True)
    username = models.ForeignKey(User,
                                to_field="username",
                                db_column="username",
                                on_delete=models.CASCADE)
    cate_name = CharField(max_length=100, unique=True)
    cate_date = DateTimeField(auto_now_add = True)
    
    class Meta:
        db_table = "CATEGORY"

        app_label = "mainapp"

        managed = False

class Community(models.Model):
    com_num = AutoField(primary_key=True)
    username = models.ForeignKey("User",
                                to_field="username",
                                db_column="username",
                                on_delete=models.CASCADE)
    cate_name = CharField(max_length=255)
    com_title = CharField(max_length=255)
    com_content = TextField()
    com_combool = CharField(max_length=1)
    com_date = DateTimeField(auto_now_add = True)
    com_count = IntegerField(default=1)
    com_path = CharField(max_length=100)
    
    class Meta:
        db_table = "Community"

        app_label = "mainapp"

        managed = False

class Comment(models.Model):
    comment_num = AutoField(primary_key=True)
    com_num = models.ForeignKey("Community",
                                to_field="com_num",
                                db_column="com_num",
                                on_delete=models.CASCADE)
    username = models.ForeignKey("User",
                                to_field="username",
                                db_column="username",
                                on_delete=models.CASCADE)
    comment_content = TextField()
    comment_create_date = DateTimeField(auto_now_add = True)
    comment_modified_date = DateTimeField(auto_now = True)
    
    class Meta:
        db_table = "COMMENT"

        app_label = "mainapp"

        managed = False
