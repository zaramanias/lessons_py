from address import Address
from mailing import Mailing

Mailing1 = Mailing(
    to_address=Address("123456", "Москва", "ул. Пушкина", "10", "5A"),
    from_address=Address("654321", "Москва", "ул. Красная", "20", "10B"),
    track="TRACK123",
    cost=1500
)

print(Mailing1)
