from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+7945678901"),
    Smartphone("Samsung", "Galaxy S21", "+79876543212"),
    Smartphone("Google", "Pixel 6", "+79223344550"),
    Smartphone("OnePlus", "9 Pro", "+79112233445"),
    Smartphone("Sony", "Xperia 1 III", "+79334455667")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
