from termcolor import colored
from pythonping import ping
print(colored("                           BruteTOOTH ","blue"))
def logo():
 lo=open("logo.txt","r")
 print(colored(lo.read(),color="blue",))
logo()
print(colored(" *developed by m00n","red",))
print(colored(" -tp to ping the target website","red",))
print(colored(" -h to show option command","red",))
def help():
 file=open("help_cmd.txt","r")
 print(file.read())
i=10000
while i>0:
 cmd=input(colored("command>>","blue",))
 if (cmd=="-h"):
  help()
 elif (cmd=="-tp"):
  addr=input(colored("target website>>","red"))
  ping(addr, verbose=True, count=1000)
 elif (cmd=="-exit"):
  print(colored("Thank For Using This Tool","white"))
  i=0
 else:
  print("ERROR COMMAND>>",format(cmd))
