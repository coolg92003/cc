#!/usr/bin/env python3.9

import subprocess
import sys
import getopt

Work_Dir = "./"
Server_Cert_Config_List = []
CA_Key_File = '/CA.key'
CA_Cert_File = '/CA.cert'
Server_Cnf_File = '/server_cert.cnf'
Server_Key_File = '/Server.key'
Server_Csr_File = '/Server.csr'
Server_Cert_File = '/Server.cert'
Input_File_Name = ''
Max_Supported_Ip_Num = 30

def run_linux_command(l_cmd, i_input=None):
    l_process = subprocess.Popen(l_cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    l_output, dummy_err = l_process.communicate(i_input)
    l_rc = l_process.poll()
    #return (l_rc, l_output)
    return (l_rc, dummy_err)

def Clean_other_files():
    cmd = "rm -rf *.cnf *.key *.crt *.csr"
    r_rc, r_output = run_linux_command(cmd)

def get_input_data():
    global CA_Key_File
    global CA_Cert_File
    global Server_Cnf_File
    global Server_Key_File
    global Server_Csr_File
    global Server_Cert_File
    global Work_Dir
    global Input_File_Name

    is_get_dir = False
    is_get_input_file = False
    input_argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(input_argv, "d:i:", ["dir=", "input_file="])
    except:
        print("get_input_data(): Error to get dir and input file" + input_argv)
        return False
    for opt, arg in opts:
        if opt in ['-d', '--dir']:
            Work_Dir = arg
            is_get_dir = True
        elif opt in ['-i', '--input_file']:
            Input_File_Name = arg
            is_get_input_file = True
    if is_get_dir == False or is_get_input_file == False:
        print("get_input_data(): Error Please check your input paras")
        return False
    else:
        CA_Key_File = Work_Dir + CA_Key_File 
        CA_Cert_File = Work_Dir + CA_Cert_File 
        Server_Cnf_File = Work_Dir + Server_Cnf_File 
        Server_Key_File = Work_Dir + Server_Key_File 
        Server_Cert_File = Work_Dir + Server_Cert_File 
        Server_Csr_File = Work_Dir + Server_Csr_File 
        Input_File_Name = Work_Dir + '/' + Input_File_Name 
    return True

    
def fill_comm_part_server_cnf_file():
    global Server_Cert_Config_List
    Server_Cert_Config_List.append('[req]')
    Server_Cert_Config_List.append('prompt = no')
    Server_Cert_Config_List.append('req_extensions = v3_req')
    Server_Cert_Config_List.append('distinguished_name = req_distinguished_name')
    Server_Cert_Config_List.append('')
    Server_Cert_Config_List.append('[req_distinguished_name]')
    Server_Cert_Config_List.append('countryName = CN')
    Server_Cert_Config_List.append('stateOrProvinceName = ShanDong')
    Server_Cert_Config_List.append('localityName = QingDao')
    Server_Cert_Config_List.append('organizationName  = Nokia')
    Server_Cert_Config_List.append('organizationalUnitName  = RD')
    Server_Cert_Config_List.append('commonName = hfed.nokia.com')
    Server_Cert_Config_List.append('emailAddress = cliff.chen@nokia-sbell.com')
    Server_Cert_Config_List.append('')
    Server_Cert_Config_List.append('[ v3_req ]')
    Server_Cert_Config_List.append('basicConstraints = CA:FALSE')
    Server_Cert_Config_List.append('keyUsage = nonRepudiation, digitalSignature, keyEncipherment')
    Server_Cert_Config_List.append('subjectAltName = @alt_names')
    Server_Cert_Config_List.append('')
    Server_Cert_Config_List.append('[alt_names]')
    Server_Cert_Config_List.append('DNS.1 = nokia.com')
    Server_Cert_Config_List.append('IP.1 = 127.0.0.1')
    Server_Cert_Config_List.append('IP.2 = ::')
    #print(Server_Cert_Config_List)
    return True

def read_input_file():
    global Server_Cert_Config_List
    #print("read_input_file: Read IP from file " + Input_File_Name);
    cnt = 0
    try:
        with open(Input_File_Name, 'r') as input_file_handler:
            all_lines = input_file_handler.readlines()
            for each_line in all_lines:
                cnt = cnt + 1
                if cnt > Max_Supported_Ip_Num:
                    print("read_input_file: The total IP num is bigger than " + str(Max_Supported_Ip_Num))
                    return False
                if each_line is None:
                    break
                new_line = 'IP.' + str(cnt) + ' = ' + each_line.rstrip()
                #print("new_line = <" + str(new_line) + ">")
                Server_Cert_Config_List.append(new_line)
    except:
        print("read_input_file: Failed to read file " + Input_File_Name);
        return False
    return True

def write_server_cnf_file():
    #print("write_server_cnf_file: Write the content into server configuration file " + Server_Cnf_File)
    try:
        with open(Server_Cnf_File, 'x') as output_file_handler:
            for each_line in Server_Cert_Config_List:
                output_file_handler.write(each_line+'\n')
    except:
        print("write_server_cnf_file: Failed to read file " + Server_Cnf_File);
        return False
    return True

def print_error_for_ca_certs(fn_name, cmd, err_output):
    print(f'{fn_name}:Error to run cmd<{cmd}>')
    err_info = err_output.decode().strip()
    print(f'{fn_name}:Error info <{err_info}>')

def create_the_ca_certs():
    '''
    Run openssl command one by one to
    1) Create CA key
    2) Create CA Cert
    3) Create server Key
    4) Create server Csr
    5) Create server Cert
    '''

    openssl_cmd = 'openssl '
    out_str = ' -out '
    in_str = ' -in '
    key_str = ' -key '

    # 1) create key: openssl genrsa -out ca.key 2048
    genrsa_str = 'genrsa '
    key_len = ' 2048'
    create_ca_key_cmd = openssl_cmd + genrsa_str + out_str + CA_Key_File + key_len
    r_rc, r_output = run_linux_command(create_ca_key_cmd)
    if r_rc != 0:
        print_error_for_ca_certs('create_the_ca_certs', create_ca_key_cmd, r_output)
        return False

    # 2) Create CA cert: openssl req -subj "/C=CN/ST=ShanDong/L=QingDao/O=Nokia/OU=RD/CN=HFED CA/emailAddress=cliff.chen@nokia-sbell.com" -new -x509 -days 3650 -key ca.key -out ca.crt
    sub_str = '-subj "/C=CN/ST=ShanDong/L=QingDao/O=Nokia/OU=RD/CN=HFED CA/emailAddress=cliff.chen@nokia-sbell.com" '
    
    days_str = '-days 3650 '
    create_ca_cert_cmd = openssl_cmd + 'req ' + sub_str + '-new -x509 ' + days_str + key_str + CA_Key_File + out_str + CA_Cert_File 
    r_rc, r_output = run_linux_command(create_ca_cert_cmd)
    if r_rc != 0:
        print_error_for_ca_certs('create_the_ca_certs', create_ca_cert_cmd, r_output)
        return False
    
    # 3) Server key and server cert
    # 3.1) server key: openssl genrsa -out server.key 2048
    create_server_key_cmd = openssl_cmd + genrsa_str + out_str + Server_Key_File + key_len
    r_rc, r_output = run_linux_command(create_server_key_cmd)
    if r_rc != 0:
        print_error_for_ca_certs('create_the_ca_certs', create_server_key_cmd, r_output)
        return False

    # 3.2) create server csr file: openssl req -new -config non_ca_cert.cnf -key server.key -out server.csr
    #      check csr file content: openssl req -text -noout -in server.csr
    create_server_csr_cmd = openssl_cmd + 'req -new -config ' + Server_Cnf_File + key_str + Server_Key_File + out_str + Server_Csr_File
    r_rc, r_output = run_linux_command(create_server_csr_cmd)
    if r_rc != 0:
        print_error_for_ca_certs('create_the_ca_certs', create_server_csr_cmd, r_output)
        return False

    # 3.3) create server cert file: openssl x509 -req -days 3650 -CA ca.crt -CAkey ca.key -set_serial 01 -in server.csr -extensions v3_req -extfile non_ca_cert.cnf -out server.crt
    #     check cert : openssl x509 -text -noout -in server.crt
    ca_key_cert_str = ' -CAkey ' + CA_Key_File + ' -CA ' + CA_Cert_File + ' -set_serial 01'
    server_csr_str = in_str + Server_Csr_File + ' -extensions v3_req -extfile ' + Server_Cnf_File
    create_server_cert_cmd = openssl_cmd + 'x509 -req ' + days_str + ca_key_cert_str + server_csr_str + out_str + Server_Cert_File
    r_rc, r_output = run_linux_command(create_server_cert_cmd)
    if r_rc != 0:
        print_error_for_ca_certs('create_the_ca_certs', create_server_cert_cmd, r_output)
        return False
    #print(create_server_cert_cmd)

    return True

def main():
    print(f'Please wait......')
    # Remove files
    Clean_other_files()

    # Process input parameters
    if get_input_data() == False:
        return

    # Fill the common part of server cert configuration file
    if fill_comm_part_server_cnf_file() == False:
        return

    # Read the file
    if read_input_file() == False:
       return

    # Write the data into cnf file
    if write_server_cnf_file() == False:
       return

    # Create certs
    if create_the_ca_certs() == False:
       return
    print(f'Congratulations!\nfiles CA.cert, Server.key, and Server.cert are created under {Work_Dir}')
    return True
if __name__ == "__main__":
    main()

