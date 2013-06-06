import argparse
import getpass
import sys
import telnetlib

def main(user_info, command_list, output, host):
  with open(output, "w") as f:
    user_file = open(user_info, "r")
    user = user_file.readline()
    passwd = user_file.readline()
    user_file.close()

    tn = telnetlib.Telnet(host)
    tn.read_until('login: ')
    tn.write(user + '\n')
    if passwd :
      tn.read_until('Password: ')
      tn.write(passwd + '\n')
    command = open(command_list, "r")
    while True :
      cmd = command.readline()
      if cmd == "":
        break
      tn.write(cmd + '\n')

    f.write(host + '\n')
    f.write(tn.read_all() + '\n')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("user_info",
      help="user account and password")
  parser.add_argument("command_list",
      help="the command list you want to put")
  parser.add_argument("output",
      help="the path of the output file")
  parser.add_argument("site_address",
      help="the link the the site")
  args = parser.parse_args()
  main(args.user_info, args.command_list,
       args.output, args.site_addr)
