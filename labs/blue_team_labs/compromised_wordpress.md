# Compromised Wordpress

**Category:** Log Analysis

**Link:** https://blueteamlabs.online/home/challenge/log-analysis-compromised-wordpress-ce000f5b59

**PCAP:** `access.log`

## Scenario:
    One of our WordPress sites has been compromised but we're currently unsure how. The primary hypothesis is that an installed plugin was vulnerable to a remote code execution vulnerability which gave an attacker access to the underlying operating system of the server. 


### PREPROCESSING
**Time range of the attack**
- head access.log && tail access.log:
    - start : [12/Jan/2021:15:52:41 +0000]
    - end : [14/Jan/2021:07:46:52 +0000]

**Take back the list of relevant ip**
```bash
cat access.log | cut -d ' ' -f1 | sort | uniq -c | sort -nr > IPs.txt 
```
> explain : cut -d : delimeter, sort : alphabetic order, uniq -c: count the number of once, sort -nr : numerical and reverse order

**Take back the user agent**
```bash
cat access.log | cut -d '"' -f6 | cut -d '[' -f1 | sort | uniq -c | sort -nr > useragents.txt 
```

**take a look in unique POST ip request**
```bash
grep "POST" access.log | grep -v '403' | cut -d ' ' -f 1 | sort | uniq -c | sort -nr
```
> explain: grep -v : exclude string or pattern containning '403' (forbidden error)
**Noticed ip=103.69.55.212**
```bash
1. grep "103.69.55.212"
2. whois 103.69.55.212
3. virussTotal : 103.69.55.212 --> it seems to be profed
```
**Beacause the website was installed an vulnerability**
***--> look at the files in http GET request***
- We see "contact-form-7" and "simple-file-list" file --> lets search to study it

**lets see what ip was most associated with these files**
```bash
grep -i 'contact' access.log
grep -i 'simple' access.log
```
***We noticed on ip=119.241.22.121***
```bash
whois 119.241.22.121 
virussTotal : 119.241.22.121 --> clear --> it seems to be profed
```
***lets check when these plugins were installed or activated***
```bash
grep -i 'contact-form-7' access.log
```
>note: this plugin was activated on [12/Jan/2021:15:57:07 +0000]

```bash
grep -i 'simple-file-list' access.log
```
>note: this plugin was activated on [12/Jan/2021:15:56:41 +0000]

> **Conclusion:** both plugins have vulnerabilities to RCE




### 01: Identify the URI of the admin login panel that the attacker gained access to (include the token)

    wp-login.php?itsec-hb-token=adminlogin
### 02: Can you find two tools the attacker used?
    WPScan sqlmap

### 03: The attacker tried to exploit a vulnerability in ‘Contact Form 7’. What CVE was the plugin vulnerable to? (Do some research!)
    CVE-2020-35489	(Common Vulnerabilities and Exposures)

### 04: What plugin was exploited to get access?
    Simple File List 4.2.2

### 05: What is the name of the PHP web shell file?
    web shell is a bunch of commands installed on web server to allows attackers can access and remotely manage
        - To : run shell commands, privilage escalation, upload/delete malwares.
    Answer: fr34k.php
### 06: What was the HTTP response code provided when the web shell was accessed for the final time?
    404
    