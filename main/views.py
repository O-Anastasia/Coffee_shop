from django.shortcuts import render
from .models import Products, Timetable


# Create your views here.
def index(request):

    context = { 'head_line_1': 'Fresh Coffee',
                'head_line_2': 'Worth Drinking',
                'description_1': '''
                                Every cup of our quality artisan coffee starts with
                                locally sourced, hand-picked ingredients.
                                Once you try it, our coffee will be a blissful
                                addition to your everyday morning routine - we guarantee it!
                                ''',
                'head_line_3': 'Visit Us Today!',
                'lower_line_1': 'Our Promise',
                'lower_line_2': 'To You',
                'description_2': '''
                                    When you walk into our shop to start your day,
                                    we are dedicated to providing you with friendly service, a welcoming atmosphere, 
                                    and above all else, excellent products made with the highest quality ingredients.
                                    If you are not satisfied, please let us know and we will do whatever we can to make things right!
                                    ''',
               }
    return render(request, 'index.html', context=context)


def about(request):

    context = { 'title_about_1': 'Strong Coffee, Strong Roots',
                'title_about_2': 'About Our Cafe',
                'description_1': '''
                                Founded in 1987 by the Hernandez brothers, 
                                our establishment has been serving up rich coffee 
                                sourced from artisan farmers in various regions of 
                                South and Central America. We are dedicated to 
                                travelling the world, finding the best coffee, 
                                and bringing back to you here in our cafe.
                                ''',
                'description_2': '''
                We guarantee that you will fall in lust with our decadent blends 
                the moment you walk inside until you finish your last sip. 
                Join us for your daily routine, an outing with friends, 
                or simply just to enjoy some alone time.''',
                }

    return render(request, 'about.html', context=context)

def products(request):

    products = Products.objects.filter(is_visible=True)
    context = { 'products': products,
                }

    return render(request, 'products.html', context=context)
def store(request):

    days = Timetable.objects.all()
    context = { 'head_line_1': 'Come On In',
                'head_line_2': "We're Open",
                'address_line_1': '1116 Orchard Street',
                'address_line_2': 'Golden Valley, Minnesota',
                'phone': '(317) 585-8468',
                'phone_propose': 'Call Anytime',

                'days': days,
                }

    return render(request, 'store.html', context=context)


