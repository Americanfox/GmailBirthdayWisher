import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day = now.day
print(day)

if day == #Enter Birthday:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        chosen_quote = random.choice(quotes)
        print(chosen_quote)

    my_email = # Insert Your Email
    password = # Insert your password
    send_email = # Insert your the persons email

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Makes connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=send_email,
            msg=f"Subject: Happy Birthday\n\n{chosen_quote}"
         )









