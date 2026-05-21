class HotelRoom:
    base_price = 100
    def __init__(self,room_number, nights_booked, guest_name):
        if HotelRoom.is_valid(nights_booked):
            self.room_number = room_number
            self.nights_booked = nights_booked
            self.guest_name= guest_name

        else:
            return


    def calculate_total_bill(self):
        return HotelRoom.base_price*self.nights_booked
    @classmethod
    def update_base_price(cls,val):
        cls.base_price = val
    @staticmethod
    def is_valid(x):
        return x>0

room1 = HotelRoom(101,2,"someone")
room2 = HotelRoom(102,-1,"someone2")
print(room1.calculate_total_bill())
HotelRoom.update_base_price(200)
print(HotelRoom.base_price)
