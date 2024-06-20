#Send ssh command to server

import argparse
import logging
import sys
import paramiko

logger = logging.getLogger("x-mitter")

INPUT_OFFSET = "                                          >> "

try:
    import paramiko
except Exception as e:
    logger.fatal("Can't import paramiko library. Are you sure that you installed paramiko?")
    logger.fatal(f"Import Error: {e}")
    logger.fatal("You can install it via: 'pip install paramiko'")
    logger.fatal("Press Enter multiple times to exit")
    input(INPUT_OFFSET)
    exit()

#setuplogging method
def setuplogging():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#parse arguments method
def parse_args():
    parser = argparse.ArgumentParser(description='Interactive ssh console')
    parser.add_argument(option_string='-sa', option_string='--server_address', type=str, help='server address')
    parser.add_argument(option_string='-sp', option_string='--server_port', type=int, help='server port')
    parser.add_argument(option_string='-u', option_string='--username', type=str, help='username')
    parser.add_argument(option_string='-p', option_string='--password', type=str, help='password')
    parser.add_argument(option_string='-c', option_string='--command', type=str, help='ssh command')
    return parser.parse_args()

#is_valid_ip method
def is_valid_ip(address):
    try:
        octets = address.split('.')
        octets = [octet for octet in octets if len(octet) <= 3] 
        valid = [int(b) for b in octets]
        valid = [b for b in valid if b >= 0 and b<=255]
        return len(octets) == 4 and len(valid) == 4
    except:
        return False

#create ssh connection method
def _create_ssh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return ssh

#connect to ssh server method
def connect_to_ssh_server(server_address, server_port, username, password):
    ssh = _create_ssh()
    ssh.connect(server_address, port=server_port, username=username, password=password)
    return ssh

#execute ssh command method
def execute_ssh_command(command, ssh_server):
    stdin, stdout, stderr = ssh_server.exec_command(command)
    print(stdout.read().decode('utf-8'))
    print(stderr.read().decode('utf-8'))

#upload file to ssh server
def send_file_to_ssh_server(local_file_path, remote_file_path, ssh_server):
    sftp = ssh_server.open_sftp()
    sftp.put(local_file_path, remote_file_path)
    sftp.close()

#download file from ssh server
def receive_file_from_ssh_server(remote_file_path, local_file_path, ssh_server):
    sftp = ssh_server.open_sftp()
    sftp.get(remote_file_path, local_file_path)
    sftp.close()

#invoke ssh shell
def invoke_ssh_shell(ssh_server):
    ssh_server.invoke_shell()
    ssh_server.settimeout(1)
    while True:
        try:
            line = ssh_server.recv(9999).decode('utf-8')
            print(line)
        except Exception as e:
            logger.error(f"Error: {e}")
            break
    ssh_server.close()

#close ssh connection method
def close_ssh_connection(ssh_server):
    ssh_server.close()

#main method
def main():
    # arguments
    # argv[1]:server_address, exp:'192.168.127.12'
    # argv[2]:server_port, exp:22
    # argv[3]:username, exp:'root'
    # argv[4]:password, exp:'123'
    setuplogging()
    logger.info('Usage: python3 ssh_command.py server_address server_port username password command')
    args = parse_args()
    logger.debug(f"Programm was called with the following arguments: {vars(args)}")
    ssh_server = connect_to_ssh_server(server_address=args.server_address, server_port=args.server_port, username=args.username, password=args.password)
    execute_ssh_command(command=args.command, ssh_server=ssh_server)
    close_ssh_connection(ssh_server=ssh_server)

if __name__ == '__main__':
    main()
