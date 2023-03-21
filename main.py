import smtplib

# TODO: How to send Emails with python using SMTP
# my_email = "luke.m.j.stevens@gmail.com"
# password = "sickoihqzamyqtke"
# send_email = "mikayla.standridge1@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()  # Makes connection secure
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=send_email,
#         msg="Subject: Hello Little Woman\n\n Come bend over daddies lap so i can fist both your holes"
#     )

# TODO: Working with the datetime Module
import datetime as dt
import random


now = dt.datetime.now()
day = now.day
print(day)

if day == 3:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        chosen_quote = random.choice(quotes)
        print(chosen_quote)

    my_email = "luke.m.j.stevens@gmail.com"
    password = "sickoihqzamyqtke"
    send_email = "mikayla.standridge1@gmail.com"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Makes connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_email,
            msg=f"Subject: Hello Little Woman\n\n{chosen_quote}"
         )









