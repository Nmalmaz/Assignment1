import enum


# Enum for room type
class RoomType(enum.Enum):
    Single = 1
    Double = 2


# Class for Guest
class Guest:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone

    # Getter and Setter methods
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone

    # String function to get the class
    def __str__(self):
        return Guest.__str__(self) + " " + str(self.__name) + " " + str(self.__email) + " " + str(self.__phone)


# Class for Hotel
class Hotel:
    def __init__(self, hotel_name, address, phone):
        self.__hotel_name = hotel_name
        self.__address = address
        self.__phone = phone

    # Getter and Setter methods
    def getHotelName(self):
        return self.__hotel_name

    def setHotelName(self, hotel_name):
        self.__hotel_name = hotel_name

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone

    # Updated getAvailability method to accept room_number
    def getAvailability(self, room_number):
        available_rooms = ["1", "2", "3", "4"]  # Example list of available rooms
        if room_number in available_rooms:
            return True
        return False

    # String function to get the class
    def __str__(self):
        return Hotel.__str__(self) + " " + str(self.__hotel_name) + " " + str(self.__address) + " " + str(self.__phone)


# Class for Room
class Room:
    def __init__(self, room_number="", room_type=RoomType.Single, price=100, smoking_allowed=False, features=None):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__price = price  # Room price
        self.__smoking_allowed = smoking_allowed
        self.__features = features if features is not None else []

    # Getter and Setter methods
    def setRoomNumber(self, room_number):
        self.__room_number = room_number

    def getRoomNumber(self):
        return self.__room_number

    def setRoomType(self, room_type):
        self.__room_type = room_type

    def getRoomType(self):
        return self.__room_type

    def setPrice(self, price):
        self.__price = price

    def getPrice(self):
        return self.__price

    def setSmokingAllowed(self, smoking_allowed):
        self.__smoking_allowed = smoking_allowed

    def getSmokingAllowed(self):
        return self.__smoking_allowed

    def setFeatures(self, features):
        self.__features = features

    def getFeatures(self):
        return self.__features

    # Method to calculate room cost based on the number of nights
    def calculateRoomCost(self, number_of_nights):
        return self.__price * number_of_nights

    # String function to get the class
    def __str__(self):
        return Room.__str__(self) + " " + str(self.__room_number) + " " + str(self.__room_number) + " " + str(
            self.__price) + " " + str(self.__smoking_allowed) + " " + str(self.__features)


# Class for Billing
class Billing:
    def __init__(self, billing_name, credit_card_type, credit_card_last_digits, room_cost_per_night, room_subtotal,
                 taxes_and_fees, total_charges):
        self.__billing_name = billing_name
        self.__credit_card_type = credit_card_type
        self.__credit_card_last_digits = credit_card_last_digits
        self.__room_cost_per_night = room_cost_per_night
        self.__room_subtotal = room_subtotal
        self.__taxes_and_fees = taxes_and_fees
        self.__total_charges = total_charges

    # Getter and Setter methods
    def getBillingName(self):
        return self.__billing_name

    def setBillingName(self, billing_name):
        self.__billing_name = billing_name

    def getCreditCardType(self):
        return self.__credit_card_type

    def setCreditCardType(self, credit_card_type):
        self.__credit_card_type = credit_card_type

    def getCreditCardLastDigits(self):
        return self.__credit_card_last_digits

    def setCreditCardLastDigits(self, credit_card_last_digits):
        self.__credit_card_last_digits = credit_card_last_digits

    def getRoomCostPerNight(self):
        return self.__room_cost_per_night

    def setRoomCostPerNight(self, room_cost_per_night):
        self.__room_cost_per_night = room_cost_per_night

    def getRoomSubtotal(self):
        return self.__room_subtotal

    def setRoomSubtotal(self, room_subtotal):
        self.__room_subtotal = room_subtotal

    def getTaxesAndFees(self):
        return self.__taxes_and_fees

    def setTaxesAndFees(self, taxes_and_fees):
        self.__taxes_and_fees = taxes_and_fees

    def getTotalCharges(self):
        return self.__total_charges

    def setTotalCharges(self, total_charges):
        self.__total_charges = total_charges

    # String function to get the class
    def __str__(self):
        return Billing.__str__(self) + " " + str(self.__billing_name) + " " + str(self.__credit_card_type) + " " + str(
            self.__credit_card_last_digits) + " " + str(self.__room_cost_per_night) + " " + str(
            self.__room_subtotal) + " " + str(self.__taxes_and_fees) + " " + str(self.__total_charges)


# Class for Reservation
class Reservation:
    def __init__(self, reservation_number, trip_number, hotel_confirmation_number, check_in_date, check_in_time,
                 check_out_date, check_out_time, number_of_nights, number_of_rooms):
        self.__reservation_number = reservation_number
        self.__trip_number = trip_number
        self.__hotel_confirmation_number = hotel_confirmation_number
        self.__check_in_date = check_in_date
        self.__check_in_time = check_in_time
        self.__check_out_date = check_out_date
        self.__check_out_time = check_out_time
        self.__number_of_nights = number_of_nights
        self.__number_of_rooms = number_of_rooms

    # Getter and Setter methods
    def getReservationNumber(self):
        return self.__reservation_number

    def setReservationNumber(self, reservation_number):
        self.__reservation_number = reservation_number

    def getTripNumber(self):
        return self.__trip_number

    def setTripNumber(self, trip_number):
        self.__trip_number = trip_number

    def getHotelConfirmationNumber(self):
        return self.__hotel_confirmation_number

    def setHotelConfirmationNumber(self, hotel_confirmation_number):
        self.__hotel_confirmation_number = hotel_confirmation_number

    def getCheckInDate(self):
        return self.__check_in_date

    def setCheckInDate(self, check_in_date):
        self.__check_in_date = check_in_date

    def getCheckInTime(self):
        return self.__check_in_time

    def setCheckInTime(self, check_in_time):
        self.__check_in_time = check_in_time

    def getCheckOutDate(self):
        return self.__check_out_date

    def setCheckOutDate(self, check_out_date):
        self.__check_out_date = check_out_date

    def getCheckOutTime(self):
        return self.__check_out_time

    def setCheckOutTime(self, check_out_time):
        self.__check_out_time = check_out_time

    def getNumberOfNights(self):
        return self.__number_of_nights

    def setNumberOfNights(self, number_of_nights):
        self.__number_of_nights = number_of_nights

    def getNumberOfRooms(self):
        return self.__number_of_rooms

    def setNumberOfRooms(self, number_of_rooms):
        self.__number_of_rooms = number_of_rooms

    # Method to calculate total cost
    def calculateTotal(self, room_price_per_night, taxes_and_fees):
        room_cost = room_price_per_night * self.__number_of_nights * self.__number_of_rooms
        total_cost = room_cost + taxes_and_fees
        return total_cost

    # String function to get the class
    def __str__(self):
        return Reservation.__str__(self) + " " + str(self.__reservation_number) + " " + str(
            self.__trip_number) + " " + str(self.__hotel_confirmation_number) + " " + str(
            self.__check_in_date) + " " + str(self.__check_in_time) + " " + str(self.__check_out_date) + " " + str(
            self.__check_out_time) + " " + str(self.__number_of_nights) + " " + str(self.__number_of_rooms) + " " + str(
            self.__check_out_time)


# Creating Room example for Abu Dhabi Hotel with features
room1 = Room(room_number="1", room_type=RoomType.Double, price=89.95, smoking_allowed=False,
             features=[
                 "2 Queen Beds" + "/" + "No Smoking" + "/" + "Desk" + "/" + "Safe" + "/" + "Coffee Maker In Room" + "/" + "Hair Dryer"])

# Creating Guest example
guest = Guest(name="Ted H Vera", email="tedvera@mac.com", phone="")

# Creating Hotel example for Abu Dhabi Hotel
hotel = Hotel(hotel_name="Abu Dhabi Hotel", address="123 Corniche Road, Abu Dhabi, UAE",
              phone="02-884-0000")

# Creating Reservation example for 2 nights
reservation = Reservation(reservation_number="52523687", trip_number="15549850358",
                          hotel_confirmation_number="52523687", check_in_date="Sun, Aug 22, 2010",
                          check_in_time="3:00 PM", check_out_date="Tue, Aug 24, 2010", check_out_time="12:00 PM",
                          number_of_nights=2, number_of_rooms=1)

# Calculating total room cost
room_subtotal = room1.calculateRoomCost(reservation.getNumberOfNights())  # $179.90 for 2 nights

# Creating Billing instance with the total room charges, taxes, and fees
billing = Billing(billing_name="Ted H Vera", credit_card_type="Mastercard", credit_card_last_digits="9904",
                  room_cost_per_night=room1.getPrice(), room_subtotal=room_subtotal,
                  taxes_and_fees=21.58, total_charges=201.48)

# Displaying reservation details
print("Your Reservation is Confirmed!")
print("Thank you for your reservation. Please print your hotel receipt and show it at check in.")

print("Guest Name:", guest.getName())
print("Email:", guest.getEmail())
print("Priceline Trip Number:", reservation.getTripNumber())
print("Hotel Confirmation Number:", reservation.getHotelConfirmationNumber())

print("Abu Dhabi Hotel")

print("Hotel Name:", hotel.getHotelName())
print("Hotel Address:", hotel.getAddress())
print("Phone:", hotel.getPhone())
print("Check-In :", reservation.getCheckInDate(), "-", reservation.getCheckInTime())
print("Check-Out Date:", reservation.getCheckOutDate(), "-", reservation.getCheckOutTime())
print("Number of Nights:", reservation.getNumberOfNights())
print("Number of Rooms:", reservation.getNumberOfRooms())

print("Room 1:", guest.getName())
print("Room Type:", '."+'.join(room1.getFeatures()))

print("Summary of Charges")

print("Billing Name:", guest.getName())
print("Credit Card:", billing.getCreditCardType(), "(ending in", billing.getCreditCardLastDigits() + ")")
print("Room Cost (per night): $", room1.getPrice())
print("Rooms:", reservation.getNumberOfRooms())
print("Nights:", reservation.getNumberOfNights())

print("Room Subtotal: $", billing.getRoomSubtotal())
print("Taxes and Fees: $", billing.getTaxesAndFees())
print("Total Charges: $", billing.getTotalCharges())

# Checking availability
if hotel.getAvailability(room1.getRoomNumber()):
    print(f"Room {room1.getRoomNumber()} is available.")
else:
    print(f"Room {room1.getRoomNumber()} is not available.")

# Calculating total reservation cost
total_cost = reservation.calculateTotal(room1.getPrice(), billing.getTaxesAndFees())
print(f"Total cost for the reservation: ${total_cost}")