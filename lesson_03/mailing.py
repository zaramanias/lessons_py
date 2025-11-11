from address import Address


class Mailing:
    def __init__(self, to_address: Address, from_address: Address, cost: int,
                 track: str):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = int(cost)
        self.track = str(track)

    def __str__(self):
        return (f"Отправление {self.track} из "
                f"{self.from_address.zipcode}, {self.from_address.city}, "
                f"{self.from_address.street}, "
                f"{self.from_address.house_number} - "
                f"{self.from_address.apartment_number} в "
                f"{self.to_address.zipcode}, {self.to_address.city}, "
                f"{self.to_address.street}, "
                f"{self.to_address.house_number} - "
                f"{self.to_address.apartment_number}. "
                f"Стоимость: {self.cost} руб."
                )
