
from app.models import *
from app.utils.utils import parse_price

products = []
grouped = {}   # this will hold brand → list[Product]

def load_products_data():
    global products, grouped

    products = [

        # Vivo
        Product(id=1, name="Vivo Y21", description="Budget Friendly", price="30k", quantity=20),
        Product(id=2, name="Vivo V25", description="Budget Friendly", price="32k", quantity=18),
        Product(id=3, name="Vivo Y35", description="Budget Friendly", price="28k", quantity=22),
        Product(id=4, name="Vivo X70", description="Budget Friendly", price="40k", quantity=15),

        # Samsung
        Product(id=5, name="Samsung Galaxy A54", description="Mid-range with AMOLED display", price="45k", quantity=15),
        Product(id=6, name="Samsung Galaxy M34", description="Mid-range with AMOLED display", price="38k", quantity=20),
        Product(id=7, name="Samsung Galaxy S21 FE", description="Mid-range with AMOLED display", price="50k", quantity=10),
        Product(id=8, name="Samsung Galaxy A14", description="Mid-range with AMOLED display", price="22k", quantity=25),

        # iPhone
        Product(id=9, name="iPhone 12", description="Premium flagship device", price="65k", quantity=12),
        Product(id=10, name="iPhone 13", description="Premium flagship device", price="75k", quantity=10),
        Product(id=11, name="iPhone 14", description="Premium flagship device", price="85k", quantity=9),
        Product(id=12, name="iPhone 15", description="Premium flagship device", price="1.2L", quantity=8),

        # Realme
        Product(id=13, name="Realme 9 Pro", description="Value-for-money smartphone", price="25k", quantity=30),
        Product(id=14, name="Realme Narzo 50", description="Value-for-money smartphone", price="18k", quantity=35),
        Product(id=15, name="Realme C55", description="Value-for-money smartphone", price="15k", quantity=40),
        Product(id=16, name="Realme GT Neo 3", description="Value-for-money smartphone", price="36k", quantity=20),

        # OnePlus
        Product(id=17, name="OnePlus Nord CE 3", description="Smooth performance & UI", price="30k", quantity=20),
        Product(id=18, name="OnePlus 11R", description="Smooth performance & UI", price="45k", quantity=15),
        Product(id=19, name="OnePlus Nord 2T", description="Smooth performance & UI", price="28k", quantity=22),
        Product(id=20, name="OnePlus 10 Pro", description="Smooth performance & UI", price="55k", quantity=12),

        # Xiaomi / Redmi / Poco
        Product(id=21, name="Redmi Note 12", description="Affordable phone with strong battery", price="18k", quantity=40),
        Product(id=22, name="Redmi 10 Prime", description="Affordable phone with strong battery", price="14k", quantity=50),
        Product(id=23, name="Xiaomi 11 Lite", description="Affordable phone with strong battery", price="22k", quantity=35),
        Product(id=24, name="Poco X5 Pro", description="Affordable phone with strong battery", price="20k", quantity=30),

        # Oppo
        Product(id=25, name="Oppo F21 Pro", description="Great camera and design", price="32k", quantity=25),
        Product(id=26, name="Oppo Reno 8", description="Great camera and design", price="36k", quantity=18),
        Product(id=27, name="Oppo A78", description="Great camera and design", price="20k", quantity=28),
        Product(id=28, name="Oppo F19", description="Great camera and design", price="18k", quantity=30),

        # Motorola
        Product(id=29, name="Moto G62", description="Clean UI & durable build", price="22k", quantity=18),
        Product(id=30, name="Moto Edge 40", description="Clean UI & durable build", price="30k", quantity=12),
        Product(id=31, name="Moto G32", description="Clean UI & durable build", price="15k", quantity=25),
        Product(id=32, name="Moto E13", description="Clean UI & durable build", price="10k", quantity=35),

        # Nothing
        Product(id=33, name="Nothing Phone 1", description="Unique transparent design", price="30k", quantity=20),
        Product(id=34, name="Nothing Phone 2", description="Unique transparent design", price="40k", quantity=12),
        Product(id=35, name="Nothing Phone 2a", description="Unique transparent design", price="26k", quantity=25),
        Product(id=36, name="Nothing CMF Phone 1", description="Unique transparent design", price="18k", quantity=30),

        # ROG
        Product(id=37, name="ROG Phone 5", description="Gaming powerhouse phone", price="55k", quantity=10),
        Product(id=38, name="ROG Phone 6", description="Gaming powerhouse phone", price="65k", quantity=8),
        Product(id=39, name="ROG Phone 6D", description="Gaming powerhouse phone", price="70k", quantity=6),
        Product(id=40, name="ROG Phone 7", description="Gaming powerhouse phone", price="75k", quantity=5)
    ]
    products.sort(key=lambda p: parse_price(p.price))
    grouped = {}
    for ele in products:
        brand = ele.name.split()[0].lower()
        grouped.setdefault(brand, []).append(ele)