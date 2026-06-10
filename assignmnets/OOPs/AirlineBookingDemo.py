# ******************************************************
# Use Case: Flight class with Passenger Capacity Checks
# ******************************************************
#
# Problem Statement: Write a Python program that creates a Passenger class and a Flight class.
# The Flight class should manage a list of Passenger objects and block further bookings
# when the seat capacity is reached.
#
# Purpose: This exercise models a real-world object composition scenario where one class owns and manages a
# collection of another class. It also teaches boundary enforcement,
# where business rules (capacity limits) are built directly into the class methods.
#
# Given Input: A Flight with capacity 2, then three booking attempts
#
# Expected Output:
#
# Alice booked on Flight AI202.
# Bob booked on Flight AI202.
# Sorry, Flight AI202 is fully booked.


class Passenger:

    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city

    def update_email(self, email):
        self.email = email

    def passenger_details(self):
        print("passenger name {}, email {}, city {}".format(self.name, self.email, self.city))


class FlightBooking:
    def __init__(self):
        self.flight_list = ["BLR-8009", "MUM-232", "NY-1290", "BLR-3008"]
        self.flight_booking = {}
        self.__init_flight_booking()

    def __init_flight_booking(self):
        for flight in self.flight_list:
            self.flight_booking[flight] = []

    def show_all_flight_booking_details(self):
        for flight in self.flight_list:
            pass_list = self.flight_booking[flight]
            print("total {} passengers in flight {}".format(len(pass_list), flight))
            for p in pass_list:
                print(p.name, end=" ")
            print()

    def show_flight_booking_details(self, flight_no):
        passenger_list = self.flight_booking[flight_no]
        print("passengers in flight no ", flight_no)
        for passenger in passenger_list:
            print(passenger.name, end=" ")

    def display_flight_list(self):
        print("Below are the current available flights ")
        for flight in self.flight_list:
            print(flight, end=" ")
        print()

    def book_flight(self, flight_no, passenger):
        booked_pass = self.flight_booking[flight_no]
        if len(booked_pass) >= 2:
            for pa in booked_pass:
                print("{} booked on Flight {} ".format(pa.name, flight_no))
            print("Sorry, Flight {} is fully booked".format(flight_no))
        else:
            booked_pass.append(passenger)
            self.flight_booking[flight_no] = booked_pass
            print("passenger {} booked in flight {} successfully !!".format(passenger.name, flight_no))


def main() -> None:
    flight_booking = FlightBooking()

    while True:
        print("""
        1. show all available flights
        2. book flight for passenger
        3. all flight booking details
        4. display passengers in flight
        4. exit""")

        choice = int(input("please select options : "))

        if choice == 1:
            flight_booking.display_flight_list()
        elif choice == 2:
            flight_no = input("Enter flight no to book : ")
            name = input("Enter passenger name : ")
            email = input("Enter passenger email : ")
            city = input("Enter passenger city : ")
            passenger = Passenger(name, email, city)
            flight_booking.book_flight(flight_no, passenger)
        elif choice == 3:
            flight_booking.show_all_flight_booking_details()
        elif choice == 4:
            flight_no = input("please enter flight no : ")
            flight_booking.show_flight_booking_details(flight_no)
        else:
            break


if __name__ == "__main__":
    main()
