# IP_and_dns_server’s_names_from_domain
This small script performs the task of
determining ip address, and the dns server’s names from a domain name.

Script:

	checks all domain names from file with name "domains",
	finds unique domains and then works with list of this unique domains.


Usage
------
Create a file with name "domains", and put domains that you interesting.

(An example of this file you can find in this repository)

Attention: a file "domains" must not contain any empty line.

#####Run script

	python define_ip_ns.py

Script creates a file with name "out" in current folder with results of it work.

Each time when you run this script, file "out" will be rewrite (an old results will be delete).

Be careful with this point.

 
Requirements
------------
python 2.7

	pip dnspython==1.12.0
