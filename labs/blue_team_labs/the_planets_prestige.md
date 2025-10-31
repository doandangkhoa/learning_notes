# The planet's prestige 

**Category** : phishing email

**Link** : https://blueteamlabs.online/home/challenge/the-planets-prestige-e5beb8e545

**Scenario**

![alt text](image.png)

## 01. What is the email service used by the malicious actor?
![alt text](image-1.png)

I look at the received fields and noticed that the first one seems to be suspicous.

## 02. What is the Reply-To email address? 
![alt text](image-2.png)

## 03. What is the filetype of the received attachment which helped to continue the investigation? 
![alt text](image-3.png)

I decode the content from base64 and convert it to hexadicimal code. I notice in first 4 bytes (it's specified as a file format)

![alt text](image-4.png)

by searching, I find out the format of the file is "ZIP" while in the email, this file is pdf format ?? --> this thing seems to be like phishing

![alt text](image-5.png)

## 04. What is the name of the malicious actor?


## 05. What is the location of the attacker in this Universe? 

## 06. What could be the probable C&C domain to control the attacker’s autonomous bots?