from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Article, Partner, Company, FAQ, Employee, Vacancy, PrivacyPolicy
from .forms import FAQForm
from cart.forms import CartAddProductForm


def home(request):
    # Получаем последнюю опубликованную статью
    latest_article = Article.objects.latest('pub_date')

    # Получаем список компаний-партнеров
    partners = Partner.objects.all()

    context = {
        'latest_article': latest_article,
        'partners': partners,
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
# def faq(request):
#     faqs = FAQ.objects.all().order_by('-date_added')
#     show_question_form = request.method == 'GET'  # Показать форму только при GET-запросе
#     form = FAQForm() if show_question_form else None
#
#     if request.method == 'POST':
#         form = FAQForm(request.POST)
#         if form.is_valid():
#             question = form.cleaned_data['question']
#             user_name = form.cleaned_data['user_name']
#             faq = FAQ(question=question, user_name=user_name)
#             faq.save()
#             return redirect('shop:faq')
#
#     return render(request, 'faq.html', {'faqs': faqs, 'show_question_form': show_question_form, 'form': form})
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
