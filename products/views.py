from django.shortcuts import render


def index(request):
    context = {
        'tittle': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'tittle': 'Store - Каталог',
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {
                'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': 23725,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
            },
            {
                'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390,
                'description': 'ММатериал с плюшевой текстурой. Удобный и мягкий.',
            },
        ]
    }
    return render(request, 'products/products.html', context)
