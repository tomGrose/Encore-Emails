import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "tomgrosenbaugh@gmail.com"
toaddr = "tomgrosenbaugh@gmail.com"
cc = "tgrosenb@asu.edu"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Testing Email"
msg['Cc'] = cc

body = "Hola Muchacho"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "80123Miko?")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()