from django.contrib.sites import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Article, Partner, Company, FAQ, Employee, Vacancy, PrivacyPolicy, Review, Coupon, Advertisement
from .forms import FAQForm, ReviewForm
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm
import pytz
import datetime

from django.views.decorators.http import require_POST
from django.utils import timezone
from .forms import CouponApplyForm

def home(request):
    # Получаем последнюю опубликованную статью
    latest_article = Article.objects.latest('pub_date')

    # Получаем список компаний-партнеров
    partners = Partner.objects.all()
    user_timezone = pytz.timezone(request.session.get('user_timezone', 'UTC'))
    user_current_time = datetime.datetime.now(user_timezone)
    advertisements = Advertisement.objects.all()
    context = {
        'latest_article': latest_article,
        'partners': partners,
        'user_current_time': user_current_time,
        'advertisements': advertisements,
    }
    return render(request, 'home.html', context)


# O компании
def about_company(request):
    company = Company.objects.first()  # Получаем первую запись о компании
    return render(request, 'about_company.html', {'company': company})


# Новости
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'article_list.html', {'articles': articles})


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article_detail.html', {'article': article})


# Вопросы и ответы
def faq(request):
    faqs = FAQ.objects.all().order_by('-date_added')
    return render(request, 'faq.html', {'faqs': faqs})


def ask_question(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            user_name = form.cleaned_data['user_name']
            faq = FAQ(question=question, user_name=user_name)
            faq.save()
            return redirect('shop:faq')
    else:
        form = FAQForm()
    return render(request, 'ask_question.html', {'form': form})


# Контакты
def contact_list(request):
    employees = Employee.objects.all()
    return render(request, 'contacts.html', {'employees': employees})


def privacy_policy(request):
    privacy_policy = PrivacyPolicy.objects.first()
    return render(request, 'privacy_policy.html', {'privacy_policy': privacy_policy})


def vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies.html', {'vacancies': vacancies})

#Отзывы

@login_required
def review_list(request):
    reviews = Review.objects.all().order_by('-date_added')
    return render(request, 'review_list.html', {'reviews': reviews})

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('shop:review_list')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

#Купоны
@login_required
def coupons(request):
    active_coupons = Coupon.objects.filter(active=True)
    archived_coupons = Coupon.objects.filter(active=False)
    return render(request, 'coupons.html', {'active_coupons': active_coupons, 'archived_coupons':archived_coupons})



@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')



def example_view(request):
    return render(request, 'example.html')


def test_view(request):
    return render(request, 'test.html')

def oop_view(request):
    return render(request, 'oop.html')

def youngest_view(request):
    return render(request, 'youngest_emp.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

