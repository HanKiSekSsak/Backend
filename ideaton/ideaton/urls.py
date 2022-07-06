from django.contrib import admin
from django.urls import path
from tag_list import views
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # home url 생성
    path('', views.home, name = 'home'),

    # category url 생성
    path('category/', views.category, name = 'category'),

    # 로그인 url 생성
    path('login/', account_views.login, name = 'login'),

    # 로그아웃 url 생성
    path('logout/', account_views.logout, name = 'logout'),

    # 회원가입 url 생성
    path('signup/', account_views.signup, name = 'signup'),

    # tag url 생성
    path('tag_list/', views.tag, name = 'tag'),

    # tag_list에서 찌개 url 생성
    path('tag_list/jjigae/', views.jjigae, name = 'jjigae'),

    # tag_list에서 국 url 생성
    path('tag_list/soup/', views.soup, name = 'soup'),

    # tag_list에서 찜 url 생성
    path('tag_list/steam/', views.steam, name = 'steam'),

    # tag_list에서 구이 url 생성
    path('tag_list/roast/', views.roast, name = 'roast'),

    # tag_list에서 탕 url 생성
    path('tag_list/tang/', views.tang, name = 'tang'),
]
