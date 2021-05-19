import datetime as dt
import pandas as pd
import random
import smtplib
my_email = "prasadganeshhegde@gmail.com"
password = "ASLKdfghj1!"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    person_name = birthdays_dict[today]["name"]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    email_path = birthdays_dict[today]["email"]
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]", person_name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=email_path, msg=f"Subject:Happy Birthday\n\n{content}")




