from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('about_company/', views.about_company, name='about_company'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:article_id>/', views.article_detail, name='article_detail'),
    path('faq/ask/', views.ask_question, name='ask_question'),
    path('faq/', views.faq, name='faq'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/add/', views.add_review, name='add_review'),
    path('coupons/', views.coupons, name='coupons'),
    path('example/', views.example_view, name='example_view'),
    path('apply/', views.coupon_apply, name='apply'),

    path('test/', views.test_view, name='test_view'),
    path('oop/', views.oop_view, name='oop_view'),
    path('youngest_emp/', views.youngest_view, name='youngest_view'),
    path('product_list/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]
