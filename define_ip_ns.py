# coding: utf-8
import socket
import dns.resolver
import os


domain_name_file=open('domains','r')
domain_name_list=[]

for l in domain_name_file:
    domain_name_list.append(l[:-1])
domain_name_list=list(set(domain_name_list))

if os.path.exists('out'):
    os.remove('out')

out=open('out','a')

print "in the file was found %s unique domains" % len(domain_name_list)
out_list=[]
for index,domain_name in enumerate(domain_name_list):
    print "in process unique domain № ",index+1
    out_block=[]
    out_block.append(domain_name+'\n')
    try:
        ip=socket.gethostbyname(domain_name)
        out_block.append(ip+'\n')
    except:
        pass
    try:
        answers = dns.resolver.query(domain_name,'NS')
        for server in answers:
            out_block.append(str(server)+'\n')
    except:
        pass
    out_block.append('------------------------------'+'\n')
    out_list.append(out_block)

for domain_block in out_list:
    for line in domain_block:
        out.write(line)
out.close()