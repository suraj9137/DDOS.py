DDoS Attack Script

This repository contains a Python script that performs a DDoS (Distributed Denial of Service) attack on a specified target IP address and port. The script uses multi-threading to send a large number of fake HTTP requests to the target server, with the goal of overwhelming its resources and causing a denial of service.


Table of Contents :
Features
Requirements
Usage
Disclaimer


Features :
Generates random IP addresses and user agents for each request.
Uses multi-threading to send a large number of concurrent requests.
Limits the rate of requests to prevent spamming the server.
Allows the user to specify the target IP address, port, duration, and
number of threads.


Requirements : 
Python 3.x
socket module
threading module
random module
time module



Usage : 

To use the script, simply run it from the command line and provide the required arguments:

python ddos_attack.py <target_ip> <target_port> <duration> <num_threads>

For example, to send 500 concurrent requests to the target IP address testphp.vulnweb.com on port 80 for 100 seconds, run:

python ddos_attack.py testphp.vulnweb.com 80 100 500



Disclaimer : 

It is important to note that performing a DDoS attack is illegal and unethical without proper authorization. This code should only be used for educational purposes and should not be used to attack any server without permission.