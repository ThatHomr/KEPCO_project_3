from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='kakao'),
    path('kakaoLoginLogic/', views.kakaoLoginLogic),
    path('kakaoLoginLogicRedirect/', views.kakaoLoginLogicRedirect),
    path('kakaoLogout/', views.kakaoLogout),
    # GET | POST - Methods / Params | QueryString
    path('methodsCheck/<int:id>', views.methodsCheck),
]