from datetime import datetime

class Person:
    def __init__(self, person_id, name, mobile_no, email, date_of_birth, gender):
        self.person_id = person_id
        self.name = name
        self.mobile_no = mobile_no
        self.email = email
        self.date_of_birth = date_of_birth
        self.gender = gender

class Customer(Person):
    def __init__(self, customer_id, name, mobile_no, email, date_of_birth, gender):
        super().__init__(customer_id, name, mobile_no, email, date_of_birth, gender)
    

class FortuneTeller(Person):
    def __init__(self, fortune_teller_id, name, mobile_no, email, date_of_birth, gender):
        super().__init__(fortune_teller_id, name, mobile_no, email, date_of_birth, gender)


class FortuneType:
    def __init__(self, fortune_type_id, type):
        self.fortune_type_id = fortune_type_id
        self.type = type

class BookingSlot:
    def __init__(self, booking_slot_id, fortune_teller_id, date, time):
        self.booking_slot_id = booking_slot_id
        self.fortune_teller_id = fortune_teller_id
        self.date = date
        self.time = time


class Booking:
    def __init__(self, booking_id, customer_id, booking_slot_id, fortune_package_id):
        self.booking_id = booking_id
        self.customer_id = customer_id
        self.booking_slot = booking_slot_id
        self.fortune_package_id = fortune_package_id


class FortunePackage:
    def __init__(self, fortune_package_id, fortune_type_id, fortune_teller_id, price):
        self.fortune_package_id = fortune_package_id
        self.fortune_type_id = fortune_type_id
        self.fortune_teller_id = fortune_teller_id
        self.price = price


class FortuneTellerTransaction:
    def __init__(self, transaction_id, fortune_package_id, date_time, booking_id):
        self.transaction_id = transaction_id
        self.fortune_package_id = fortune_package_id
        self.date_time = date_time
        self.booking_id = booking_id


class Result:
    def __init__(self, result_id, transaction_id, result):
        self.result_id = result_id
        self.transaction_id = transaction_id
        self.result = result


class Product:
    def __init__(self, product_id, description):
        self.product_id = product_id
        self.description = description


class ProductRecommendation:
    def __init__(self, result_id, product_id):
        self.result_id = result_id
        self.product_id = product_id


class Review:
    def __init__(self, review_id, customer_id, fortune_teller_id, rating, comment, date_time):
        self.review_id = review_id
        self.customer_id = customer_id
        self.fortune_teller_id = fortune_teller_id
        self.rating = rating
        self.comment = comment
        self.date_time = date_time
