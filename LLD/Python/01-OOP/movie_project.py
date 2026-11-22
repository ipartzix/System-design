""" "
Create a class Movie with the following:
Attributes:
• movie_name -> name of the movie
• total_seats -> total seats available in the theatre
• ticket_price -> price per ticket
• booked_seats -> starts at 0
Methods:
• book_ticket(num_tickets) -> books the given number of tickets. If enough seats are available, confirm the booking and show the total amount to pay. If not, show "Sorry, not enough seats available".
"""

class Movie:

    def __init__(self, movie_name: str, total_seats: int, ticket_price: int ):
        print("="*50)
        print("Welcome to movie land")
        print("="*50)
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0


    def book_tickets(self,num_of_tickets:int):
        if num_of_tickets > self.total_seats - self.booked_seats:
            print("Sorry seats are not available")
        else:
            self.booked_seats += num_of_tickets
            self.total_seats -+ num_of_tickets    
            print("Your tickets booked")
            print(f"Total price = {self.ticket_price* num_of_tickets}\n")  

    def show_status(self)-> None:
        seats_available = self.total_seats - self.booked_seats
        print(f"Movie Name = {self.movie_name}")
        print(f"Seats available = {seats_available}")
        print(f"Total booked = {self.booked_seats}")

movie = Movie("RRR",100,199)
movie.show_status()
movie.book_tickets(60)
movie.show_status()
movie.book_tickets(60)

"""
\outout 


==================================================
Welcome to movie land
==================================================
Movie Name = RRR
Seats available = 100
Total booked = 0
Your tickets booked
Total price = 11940

Movie Name = RRR
Seats available = 40
Total booked = 60
Sorry seats are not available

"""
