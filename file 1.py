class FlightTable:
    def __init__(self):
        self.data = [
            {"Flight ID": "AI161E90", "From": "BLR", "To": "BOM", "Price": 5600},
            {"Flight ID": "BR161F91", "From": "BOM", "To": "BBI", "Price": 6750},
            {"Flight ID": "AI161F99", "From": "BBI", "To": "BLR", "Price": 8210},
            {"Flight ID": "VS171E20", "From": "JLR", "To": "BBI", "Price": 5500},
            {"Flight ID": "AS171G30", "From": "HYD", "To": "JLR", "Price": 4400},
            {"Flight ID": "AI131F49", "From": "HYD", "To": "BOM", "Price": 3499}
        ]

    def search_flights_by_city(self, city):
        for flight in self.data:
            if flight["From"] == city or flight["To"] == city:
                print(f"Flight ID: {flight['Flight ID']}, From: {flight['From']}, To: {flight['To']}, Price: {flight['Price']}")

    def search_flights_from_city(self, city):
        for flight in self.data:
            if flight["From"] == city:
                print(f"Flight ID: {flight['Flight ID']}, To: {flight['To']}, Price: {flight['Price']}")

    def search_flights_between_cities(self, city1, city2):
        for flight in self.data:
            if (flight["From"] == city1 and flight["To"] == city2) or (flight["From"] == city2 and flight["To"] == city1):
                print(f"Flight ID: {flight['Flight ID']}, Price: {flight['Price']}")

def main():
    flight_table = FlightTable()

    print("Choose a search parameter:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        city = input("Enter the city to search for: ")
        flight_table.search_flights_by_city(city)
    elif choice == 2:
        city = input("Enter the city to search for flights from: ")
        flight_table.search_flights_from_city(city)
    elif choice == 3:
        city1 = input("Enter the first city: ")
        city2 = input("Enter the second city: ")
        flight_table.search_flights_between_cities(city1, city2)
    else:
        print("Invalid choice. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    main()