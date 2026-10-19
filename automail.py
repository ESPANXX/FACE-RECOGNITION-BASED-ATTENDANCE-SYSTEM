import yagmail
import os

receiver = "dhairyavyas@live.com"  # receiver email address
body = "Attendence File"  # email body
filename = "Attendance"+os.sep+"Attendance.csv"  # attach the file

# connect to smtp server.
yag_smtp_connection = yagmail.SMTP( user="sizlingdhairya@gmail.com", password="Rjv@19032610", host='smtp.gmail.com')
# email subject
subject = 'Attendance Report'
# email content with attached file path.
contents = [body, filename]
# send the email
yag_smtp_connection.send(receiver, subject, contents)



