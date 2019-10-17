import sys
import time
import xlwt
import iptc
import psutil
import emails


def get_time():
    formater = "%s-%s-%s(%s:%s:%s)" 
    when = formater % time.localtime()[0:6]
    return when


class Xls(object):
    def __init__(self):
        self.xls = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.xls.add_sheet('sheet1', 
                        cell_overwrite_ok=True)
        self._row = 0
        self._col = 0

    def write(self, content):
        self.sheet.write(self._row, self._col, content)
        self._col = self._col + 1
    
    def movedown(self):
        self._row = self._row + 1
        self._col = 0

    def save(self, file_name):
        self.xls.save(file_name)


def prevent_sync(ip_addrs):
    table = iptc.Table(iptc.Table.FILTER)
    chain = iptc.Chain(table, "INPUT")
    
    for ip_addr in ip_addrs:
        rule = iptc.Rule()
        rule.set_protocol('tcp')
        rule.set_src(ip_addr)
        target = iptc.Target(rule, "DROP")
        rule.target = target
        chain.insert_rule(rule)
    
    table.commit()


def netstat():
    xls = Xls()
    suspicious = []
    connections = psutil.net_connections()
    
    for connection in connections:
        laddr = connection.laddr
        raddr = connection.raddr
        status = connection.status
        program = psutil.Process(connection.pid)
        if status == 'SYN_RECV':
            suspicious.append(raddr)

        lip = laddr.ip
        lport = laddr.port
        if raddr:
            fip = raddr.ip
            fport = raddr.port
        else:
            fip = '0.0.0.0'
            fport = '*'
        
        xls.write('%s:%s' % (lip,lport))
        xls.write('%s:%s' % (fip,fport))
        xls.write(program.name())
        xls.write(status)
        xls.movedown()
    
    syn_recv_addr = []
    for only_addr in set(suspicious):
        if suspicious.count(only_addr) > 30:
            syn_recv_addr.append(only_addr)
    prevent_sync(syn_recv_addr)

    file_name = '/root/netstat/N%s.xls' % get_time()
    xls.save(file_name)
    return file_name


def top():
    pids = psutil.pids()
    programs = []
    for pid in pids:
        program = psutil.Process(pid)
        info = []
        info.append(program.pid)
        info.append(program.name())
        info.append(program.status())
        info.append(program.username())
        info.append(round(program.memory_percent(),3))
        programs.append(info)
    programs.sort(key=lambda x:x[4], reverse=True)

    xls = Xls()
    for program in programs[0:30]:
        xls.write(program[0])
        xls.write(program[1])
        xls.write(program[2])
        xls.write(program[3])
        xls.write(program[4])
        xls.movedown()
    file_name = '/root/top/T%s.xls' % get_time()
    xls.save(file_name)
    return file_name


if __name__ == "__main__":
    email = emails.Email()
    entrance = sys.argv[1]
    if entrance == 'top':
        file_name = top()
        if sys.argv[2] == '1':
            email.send("内存状态", ' ', file_name)
        sys.exit(0)
    if entrance == 'netstat':
        file_name = netstat()
        if sys.argv[2] == '1':
            email.send("网络状态", ' ', file_name)
        sys.exit(0)
