import smtplib

email_transmitter = "your email"
password = "your password"
email_receiver= "receiver email"
message = "your message"

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.starttls
server.login(email_transmitter,password)

for i in range(0,0):                          
    server.sendmail(email_transmitter, email_receiver, message)
    print("Sent messages:", i)
server.quit()

# By @Andresgbe
