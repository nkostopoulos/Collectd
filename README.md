# Collectd

parser.py: a script to parse RRDfiles (parses DNS info)  
client.py: the /etc/collectd/collectd.conf configuration file of client  
server.py: the /etc/collectd/collectd.conf configuration file of server  
  
some notes:  
- Network plugin: to deliver UDP datagrams over the network to the Collectd Server. We should define the IP of the server  
both in the client and the server configuration file. It is Listen for the server and Server for the client. We also define  
the port at the server.  
- DNS plugin: for DNS  
- CPU plugin: for CPU information
- RRDtool plugin: for RRDfiles  
  
Interval: interval of data delivery.  
