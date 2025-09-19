from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.paginator import Paginator


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not username or not password:
            messages.error(request, "Both username and password are required.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home')
    
    return render(request, 'login.html')

def signup_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('signup')

        try:
            validate_password(password)  # Ensure strong password
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
        except ValidationError as e:
            messages.error(request, " ".join(e.messages))
            return redirect('signup')

    return render(request, 'signup.html')

def logout_user(request):
    logout(request)
    return redirect('home')                     

all_videos = {
        "HTML": [
            {"title": "Intro to HTML", "video_url": "https://www.youtube.com/embed/2oCN2q1x3c4", "vip": False},
            {"title": "HTML Hyperlinks", "video_url": "https://www.youtube.com/embed/ZOI7Tq5Zq2s", "vip": False},
            {"title": "HTML Images", "video_url": "https://www.youtube.com/embed/sm5hTFzSs5Y", "vip": False},
            {"title": "HTML Audio", "video_url": "https://www.youtube.com/embed/uof_zYxtnp0", "vip": False},
            {"title": "HTML Vedio", "video_url": "https://www.youtube.com/embed/BAx2GaMW2qA", "vip": False},
            {"title": "HTML Text Formating", "video_url": "https://www.youtube.com/embed/SZfoOAv9tEo", "vip": False},
            {"title": "HTML Lists", "video_url": "https://www.youtube.com/embed/-kXZvKxs9oA", "vip": False},
            {"title": "HTML Tables", "video_url": "https://www.youtube.com/embed/iDA0kF5lrVk", "vip": False},
            {"title": "HTML Colors", "video_url": "https://www.youtube.com/embed/6IQz_cF-Slk", "vip": False},
            {"title": "HTML Span & Div", "video_url": "https://www.youtube.com/embed/yHX-UwAnoqk", "vip": False},
            {"title": "HTML Meta tags", "video_url": "https://www.youtube.com/embed/bi5bfH_gVWE", "vip": False},
            {"title": "HTML iframes", "video_url": "https://www.youtube.com/embed/aRGdDy18qfY", "vip": False},
            {"title": "HTML Buttons", "video_url": "https://www.youtube.com/embed/_2wARy-oevQ", "vip": False},
            {"title": "HTML Forms", "video_url": "https://www.youtube.com/embed/2O8pkybH6po", "vip": False},
        ],
        "CSS": [
            {"title": "Intro to CSS", "video_url": "https://www.youtube.com/embed/xv-bBxaa7WU", "vip": False},
            {"title": "Flexbox", "video_url": "https://www.youtube.com/embed/UzURcO1MnEU", "vip": False},
            {"title": "CSS Grid", "video_url": "https://www.youtube.com/embed/6RuzhtsbSIg", "vip": False},
            {"title": "CSS Animation", "video_url": "https://www.youtube.com/embed/YA8ZciJa64k", "vip": False},
            {"title": "CSS Animation", "video_url": "https://www.youtube.com/embed/2ZlVV0MM1a0", "vip": False},
            {"title": "CSS Animation", "video_url": "https://www.youtube.com/embed/xIJvkm-CgFQ", "vip": False},
            {"title": "CSS Animation", "video_url": "https://www.youtube.com/embed/Pp7UXS3P6jY", "vip": False},
            {"title": "CSS Animation", "video_url": "https://www.youtube.com/embed/fWnXVwULqrE", "vip": False},
            {"title": "CSS Animation", "video_url": "https://www.youtube.com/embed/tb1ou6W5M5s", "vip": False},
            {"title": "CSS Animation", "video_url": "https://www.youtube.com/embed/qTEDcXJ-dzw", "vip": False},
            {"title": "CSS Animation", "video_url": "https://www.youtube.com/embed/dHpMIy517E4", "vip": False},
            {"title": "CSS Animation", "video_url": "https://www.youtube.com/embed/aii2itPgRVs", "vip": False},
            {"title": "CSS Animation", "video_url": "https://www.youtube.com/embed/O7mTUtHDP5E", "vip": False},
        ],
        "JavaScript": [
            {"title": "Intro to JavaScript", "video_url": "https://www.youtube.com/embed/Ihy0QziLDf0", "vip": False},
            {"title": "JavaScript Variables", "video_url": "https://www.youtube.com/embed/nbX0MIV7-Ek", "vip": False},
            {"title": "JavaScript Arithmetic Operators", "video_url": "https://www.youtube.com/embed/FyGIKD2fxIo", "vip": False},
            {"title": "JavaScript User Input", "video_url": "https://www.youtube.com/embed/JeXqaKeJSRI", "vip": False},
            {"title": "JavaScript Constants", "video_url": "https://www.youtube.com/embed/jLRnuVHwHKk", "vip": False},
            {"title": "JavaScript Type Conversion", "video_url": "https://www.youtube.com/embed/3M53uhj0D4k", "vip": False},
            {"title": "JavaScript Counter program", "video_url": "https://www.youtube.com/embed/uSJXZ3LkABE", "vip": False},
            {"title": "JavaScript Math Object", "video_url": "https://www.youtube.com/embed/uy-1WNqecnI", "vip": False},
            {"title": "JavaScript Random number generator", "video_url": "https://www.youtube.com/embed/K2upGO5Bb48", "vip": False},
            {"title": "JavaScript statements", "video_url": "https://www.youtube.com/embed/PgUXiprlg1k", "vip": False},
            {"title": "JavaScript Checked property", "video_url": "https://www.youtube.com/embed/SgxzJdqhyfw", "vip": False},
            {"title": "JavaScript Ternary Operator", "video_url": "https://www.youtube.com/embed/atS_A9HHAVo", "vip": False},
            {"title": "JavaScript Switches", "video_url": "https://www.youtube.com/embed/z2fcWdoph4U", "vip": False},
            {"title": "JavaScript String methods", "video_url": "https://www.youtube.com/embed/wssvLtVSFeI", "vip": False},
            {"title": "JavaScript String Slicing", "video_url": "https://www.youtube.com/embed/sPPGd4Lfh3s", "vip": False},
            {"title": "JavaScript Method Chaining", "video_url": "https://www.youtube.com/embed/J4YhlDsNqeE", "vip": False},
            {"title": "JavaScript Logical Operators", "video_url": "https://www.youtube.com/embed/ovWYhDVQiR8", "vip": False},
            {"title": "JavaScript Strict Equality", "video_url": "https://www.youtube.com/embed/O7aUm0AuUy4", "vip": False},
            {"title": "JavaScript While Loops", "video_url": "https://www.youtube.com/embed/TDUz9QcGPoE", "vip": False},
            {"title": "JavaScript For Loops", "video_url": "https://www.youtube.com/embed/ZOQYIWLngSU", "vip": False},
            {"title": "JavaScript Number Guessing Game", "video_url": "https://www.youtube.com/embed/maB0r59KOUk", "vip": False},
            {"title": "JavaScript Functions", "video_url": "https://www.youtube.com/embed/HFaxylC7bUc", "vip": False},
            {"title": "JavaScript Variable Scope", "video_url": "https://www.youtube.com/embed/KyqmbIkZGIo", "vip": False},
            {"title": "JavaScript Temperature Conversion Program", "video_url": "https://www.youtube.com/embed/6xrTdpIAsb0", "vip": False},
            {"title": "JavaScript Arrays", "video_url": "https://www.youtube.com/embed/yQ1fz8LY354", "vip": False},
            {"title": "JavaScript 2D Arrays", "video_url": "https://www.youtube.com/embed/SmJNeJuLmVo", "vip": False},
            {"title": "JavaScript Spread Operator", "video_url": "https://www.youtube.com/embed/RuDdltsfaVc", "vip": False},
            {"title": "JavaScript Rest Parameters", "video_url": "https://www.youtube.com/embed/ahwR1D_GAfc", "vip": False},
            {"title": "JavaScript Dice Roller program", "video_url": "https://www.youtube.com/embed/PXilNmL9U80", "vip": False},
            {"title": "JavaScript Random password generator", "video_url": "https://www.youtube.com/embed/1cdXwYEFDAg", "vip": False},
            {"title": "JavaScript Callbacks", "video_url": "https://www.youtube.com/embed/i2SPq-nb3NQ", "vip": False},
            {"title": "JavaScript forEach() method", "video_url": "https://www.youtube.com/embed/uOZWH0KEUs4", "vip": False},
            {"title": "JavaScript map() method", "video_url": "https://www.youtube.com/embed/xNQH1NbZQ0E", "vip": False},
            {"title": "JavaScript filter() method", "video_url": "https://www.youtube.com/embed/VvSEKHKFvpQ", "vip": False},
            {"title": "JavaScript reduce() method", "video_url": "https://www.youtube.com/embed/iDWtuWkuj8g", "vip": False},
            {"title": "JavaScript Funtion Expressions", "video_url": "https://www.youtube.com/embed/jDqmFt03Gy0", "vip": False},
            {"title": "JavaScript Arrow Function", "video_url": "https://www.youtube.com/embed/fRRRkognpOs", "vip": False},
            {"title": "JavaScript Objects", "video_url": "https://www.youtube.com/embed/lo7o91qLzxc", "vip": False},
            {"title": "JavaScript What is 'This'", "video_url": "https://www.youtube.com/embed/Jdlo8ZDt5Jg", "vip": False},
            {"title": "JavaScript Constructors", "video_url": "https://www.youtube.com/embed/WPmAu26LZKo", "vip": False},
            {"title": "JavaScript Classes", "video_url": "https://www.youtube.com/embed/U2vxAEiaVRY", "vip": False},
            {"title": "JavaScript Static keyword", "video_url": "https://www.youtube.com/embed/UOH4SAG3BoQ", "vip": False},
            {"title": "JavaScript Inheritance", "video_url": "https://www.youtube.com/embed/DqUPa0D2N78", "vip": False},
            {"title": "JavaScript Super keyword", "video_url": "https://www.youtube.com/embed/Cto38GpvJgg", "vip": False},
            {"title": "JavaScript Getters & Setters", "video_url": "https://www.youtube.com/embed/KQVCAnh6Afk", "vip": False},
            {"title": "JavaScript Destructuring", "video_url": "https://www.youtube.com/embed/UHZcJyVXtLo", "vip": False},
            {"title": "JavaScript Nested Objects", "video_url": "https://www.youtube.com/embed/b8gwYQ_V4K4", "vip": False},
            {"title": "JavaScript Array of Objects", "video_url": "https://www.youtube.com/embed/w9078dAjcrY", "vip": False},
            {"title": "JavaScript Sorting", "video_url": "https://www.youtube.com/embed/CTHhlx25X-U", "vip": False},
            {"title": "JavaScript Shuffle an Array", "video_url": "https://www.youtube.com/embed/FGAUekwri1Q", "vip": False},
            {"title": "JavaScript Date objects", "video_url": "https://www.youtube.com/embed/LwYwz67l1lA", "vip": False},
            {"title": "JavaScript Closures", "video_url": "https://www.youtube.com/embed/beZfCfiuIkA", "vip": False},
            {"title": "JavaScript setTimeout()", "video_url": "https://www.youtube.com/embed/shWr5DNVeCI", "vip": False},
            {"title": "JavaScript console.time()", "video_url": "https://www.youtube.com/embed/9amAW_qXv84", "vip": False},
            {"title": "JavaScript Format current easy", "video_url": "https://www.youtube.com/embed/HOMu48bTzz8", "vip": False},
            {"title": "JavaScript Build a Js compound interest calculator", "video_url": "https://www.youtube.com/embed/pq_FYp2JSLI", "vip": False},
            {"title": "JavaScript Build this Js Digital Clock", "video_url": "https://www.youtube.com/embed/2glfqa-ZbNw", "vip": False},
            {"title": "JavaScript Build this Js STOPWATCH", "video_url": "https://www.youtube.com/embed/d8-LGhKtzRw", "vip": False},
            {"title": "JavaScript ES6 Modules", "video_url": "https://www.youtube.com/embed/fl-_6d18DN0", "vip": False},
            {"title": "JavaScript What is asynchronous", "video_url": "https://www.youtube.com/embed/Coyy79wRz_s", "vip": False},
            {"title": "JavaScript Error handling", "video_url": "https://www.youtube.com/embed/NwoAZF66_Go", "vip": False},
            {"title": "JavaScript Build this Js calculator", "video_url": "https://www.youtube.com/embed/I5kj-YsmWjM", "vip": False},
            {"title": "JavaScript DOM explained", "video_url": "https://www.youtube.com/embed/NO5kUNxGIu0", "vip": False},
            {"title": "JavaScript Element Selectors", "video_url": "https://www.youtube.com/embed/FQtjI1PC5Z0", "vip": False},
            {"title": "JavaScript Navigation", "video_url": "https://www.youtube.com/embed/RKXIMnSwUcg", "vip": False},
            {"title": "JavaScript How to Add/Change HTML", "video_url": "https://www.youtube.com/embed/WCRi7y6aNrQ", "vip": False},
            {"title": "JavaScript Mouse Events", "video_url": "https://www.youtube.com/embed/g_vXSKbfUiQ", "vip": False},
            {"title": "JavaScript Key Events", "video_url": "https://www.youtube.com/embed/q32skvBgxo4", "vip": False},
            {"title": "JavaScript How to HIDE and SHOW HTML", "video_url": "https://www.youtube.com/embed/MkvHPOT4RS8", "vip": False},
            {"title": "JavaScript What are NodeLists", "video_url": "https://www.youtube.com/embed/5n3qPKgLEDc", "vip": False},
            {"title": "JavaScript classList property", "video_url": "https://www.youtube.com/embed/62qN2RcpIAE", "vip": False},
            {"title": "JavaScript Rock Paper Scissors", "video_url": "https://www.youtube.com/embed/3uKdQx-SZ5A", "vip": False},
            {"title": "JavaScript Build a Js Image Slider", "video_url": "https://www.youtube.com/embed/749ta0nvj8s", "vip": False},
            {"title": "JavaScript CALLBACK HELL", "video_url": "https://www.youtube.com/embed/NOlOw03qBfw", "vip": False},
            {"title": "JavaScript Promises", "video_url": "https://www.youtube.com/embed/NOzi4wBHn0o", "vip": False},
            {"title": "JavaScript ASYNC/AWAIT", "video_url": "https://www.youtube.com/embed/9j1dZwFEJ-c", "vip": False},
            {"title": "JavaScript JSON file", "video_url": "https://www.youtube.com/embed/r4MLHHLctKw", "vip": False},
            {"title": "JavaScript COOKIES work", "video_url": "https://www.youtube.com/embed/i7oL_K_FmM8", "vip": False},
            {"title": "JavaScript How to FETCH data from an API", "video_url": "https://www.youtube.com/embed/37vxWr0WgQk", "vip": False},
            {"title": "JavaScript Build a Js WEATHER APP", "video_url": "https://www.youtube.com/embed/VaDUGPMjzOM", "vip": False},     
        ],
        "Other": [
            {"title": "How Web Works", "video_url": "https://www.youtube.com/embed/5o8CwafCxnU", "vip": False},
        ],
        "Python": [
            {"title": "Python Basics", "video_url": "https://www.youtube.com/embed/rfscVS0vtbw", "vip": True},
            {"title": "Advanced Python", "video_url": "https://www.youtube.com/embed/HGOBQPFzWKo", "vip": True},
        ],
        "C++": [
            {"title": "C++ Beginner Tutorial", "video_url": "https://www.youtube.com/embed/vLnPwxZdW4Y", "vip": True},
            {"title": "C++ OOP Concepts", "video_url": "https://www.youtube.com/embed/MG4Ez0-3K9A", "vip": True},
        ],
        "Java": [
            {"title": "Java Programming Basics", "video_url": "https://www.youtube.com/embed/grEKMHGYyns", "vip": True},
            {"title": "Java OOP & Interfaces", "video_url": "https://www.youtube.com/embed/5u8rFbpdvds", "vip": True},
        ],
        "PostgreSQL": [
            {"title": "Intro to PostgreSQL", "video_url": "https://www.youtube.com/embed/NwXUg3nz2C0", "vip": True},
            {"title": "PostgreSQL Joins and Queries", "video_url": "https://www.youtube.com/embed/qw--VYLpxG4", "vip": True},
        ],
        "C#": [
            {"title": "C# Programming Tutorial", "video_url": "https://www.youtube.com/embed/GhQdlIFylQ8", "vip": True},
            {"title": "C# Windows Forms App", "video_url": "https://www.youtube.com/embed/WuyHFj9JdKg", "vip": True},
        ],
        "C": [
            {"title": "C Programming for Beginners", "video_url": "https://www.youtube.com/embed/KJgsSFOSQv0", "vip": True},
            {"title": "Pointers in C", "video_url": "https://www.youtube.com/embed/zuegQmMdy8M", "vip": True},
        ],
    }

def home(request):
    category = request.GET.get('category')
    selected_category = category if category else "All"
    is_vip = request.user.is_authenticated and getattr(request.user, "is_vip", False)
    
    all_courses = []
    for cat, videos in all_videos.items():
        for video in videos:
            video_with_cat = video.copy()
            video_with_cat['category'] = cat
            all_courses.append(video_with_cat)

    # Filter by selected category
    if selected_category == "All":
        filtered_courses = all_courses
    else:
        filtered_courses = [v for v in all_courses if v['category'] == selected_category]

    # Filter VIP if needed
    if is_vip:
        filtered_courses = [v for v in filtered_courses if v.get('vip')]

    # Build categories list with has_vip info
    categories = []
    for cat, videos_list in all_videos.items():
        has_vip = any(video.get('vip') for video in videos_list)
        categories.append({'name': cat, 'has_vip': has_vip})

    paginator = Paginator(filtered_courses, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {
        'videos': page_obj,
        'categories': categories,
        'selected_category': selected_category,
        'is_vip': is_vip,
    })


# Example: in your payment success view
def vip_payment_success(request):
    if request.user.is_authenticated:
        request.user.is_vip = True
        request.user.save()
    return redirect('home')  # or wherever you want