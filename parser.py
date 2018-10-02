import subprocess
import sys
import pty

def sum(item):
    sum = 0
    for number in item:
        sum += float(number)
    return sum

def get_values(arg):
    values = arg.split(":")
    values = [x.split("\n") for x in values]
    values = [x[0] for x in values]
    values = values[1:]
    return values

def save_output(command):
    proc = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    (out,err) = proc.communicate()
    outwithoutreturn = out.rstrip('\n')
    return outwithoutreturn

def do_it_for_file(file_of_interest,starting,ending):
    command = "rrdtool fetch " + file_of_interest + " AVERAGE -r 1 -s -" + str(starting) + " -e -" + str(ending) + " -a"
    out = save_output(command)
    values = get_values(out)
    summation = sum(values)
    return summation

if __name__ == "__main__":
    query = do_it_for_file("/var/lib/collectd/rrd/dns2.netmode.ece.ntua.gr/dns/dns_qtype-A.rrd",18,4)
    nxdomain = do_it_for_file("/var/lib/collectd/rrd/dns2.netmode.ece.ntua.gr/dns/dns_rcode-NXDOMAIN.rrd",18,4)
    noerror = do_it_for_file("/var/lib/collectd/rrd/dns2.netmode.ece.ntua.gr/dns/dns_rcode-NOERROR.rrd",18,4)
    print("Query: ",query)
    print("NXDOMAIN: ",nxdomain)
    print("NOERROR: ",noerror)
