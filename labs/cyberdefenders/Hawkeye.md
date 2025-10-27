# HawkEye Lab

**Catgory: Network Forensics**
**link: https://cyberdefenders.org/blueteam-ctf-challenges/hawkeye/**

## Scenario:
    An account at ur organization received an email with a download link. Suspicious network traffic was observed shortly after opening the email. As a SOC analysis, investigate and analyze exffiltration attemps.


### Q1: How many packets does the capture have?
    Roll to end of the capture, you can see the last package is 4003

### 02: At what time was the first package captured?
    Statistics --> Capture file property
    Time: 
        First package : 2019-04-11 03:37:07
        Last package : 2019-04-11 04:40:48
        Elapsed : 01:03:41
### 03: what is the duration of the capture
        Elapsed : 01:03:41

### 04: What is the most active computer at the link level?
    Statistics --> Conversation:
        00:08:02:1c:47:ae is the most active with more than 3000 sent package computer in the link level(layer2)

### 05: Manufacturer of the NIC (Network interface card) of the most active system at the link level?
    google search --> wireshark oui --> lookup:
        result: 00:08:02 Hewlett Packard

### 06: Where is the headquarter of the company that manufactured the NIC of the most active computer at the link level?
    goole search --> result : Palo Alto, Carlifornia

### 07: The organization works with private addressing and netmask /24. How many computers in the organization are involved in the capture?
    Statistic --> Endpoints -> IPv4
        I see 3 computer that belong to a network range 

### 08: What is the name of the most active computer at the network level?
    wireshark --> filter : smtp && eth.addr == 00:08:02:1c:47:ae --> Follow --> TCP stream --> Beijing-5cd1-PC  

### 09: What is the IP of the organization's DNS server?
    Wireshark --> filter : dns
        source port 53 --> ip : 10.4.10.4 is DNS server

### 10: What domain is the victim asking about in packet 204?
    In the package 204 --> Domain name system --> queries --> name: proforma-invoices.com

### 11: What is the IP of the domain in the previous question?
    In the package 204 --> Domain name system --> queries --> ip address: 217.182.138.150

### 12: Indicate the country to which the IP in the previous section belongs.
    terminal --> whois 217.182.138.150 --> country: France

### 13: What operating system does the victim's computer run?
    wireshark --> filter: http --> user agent: windows NT 6.1

### 14: 
    wireshark --> filter: http --> GET /proforma/tkraw_Protected99.exe HTTP/1.1

### 15: What is the md5 hash of the downloaded file?
    file --> export objects --> http --> save the file tkraw_Protected99.exe
    terminal --> md5sum tkraw_Protected99.exe --> file hash : 71826ba081e303866ce2a2534491a2f7

### 16: What software runs the webserver that hosts the malware?
    LiteSpeed

### 17: What is the public IP of the victim's computer?
    whireshark --> filter: smtp --> follow tcp stream --> victim's public ip : 173.66.146.112

### 18: in which country is the email server to which stolen information is sent?
        (where the country the email server is located?)
    smtp --> whois 23.229.162.69 --> Country : United states

### 19: Analyzing the first extraction of information. What software runs the email server to which the stolen data is sent?
    exim 4.91

### 20: to which email account is the stolen information sent?
    sales.del@macwinlogistics.in>

### 21 : What is the password used by the malware to send the email?
    decode base64 --> password : sales23

### 22: Which malware variant exfiltrated the data?
    hawkey key logger(predator pain) - reborn v9: a malware was designed to steal credentials from numerous application.

### 23: What are the bankofamerica access credentials? (username:password)
    roman.mcguire:P@ssw0rd$

### 24: Every how many minutes does the collected data get exfiltrated?
    wireshark --> filter:smtp --> follow tcp stream
        we see that the content was divided into fragments so that we check in every 10 minutes, the data get exfiltrated
        