class Address:
    def __init__(self, zip_code, city, street, house_number, apartment_number):
        self.zipcode = zip_code
        self.city = city
        self.street = street
        self.house_number = house_number
        self.apartment_number = apartment_number

    def __str__(self):
        return (f"{self.zipcode}, {self.city}, {self.street}, "
                f"{self.house_number} - {self.apartment_number}")
