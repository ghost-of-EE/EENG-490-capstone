from subprocess import Popen, PIPE
for i in (1, 2, 3):
    # Switch to Correct Wi-Fi Station
    cmd2 = "./Wi_Fi_Switch_%s.sh"%str(i)  # Shell command goes here
    cmd_out2 = Popen(cmd2, shell=True, stdout=PIPE)
    output2 = cmd_out2.communicate()[0].decode('utf-8')
    print(output2)
    # Once connected to the Wi-Fi Module, grab data file by opening a socket
    cmd3 = "./WebReplShell%s.sh"%str(i)
    cmd_out3 = Popen(cmd3, shell=True, stdout=PIPE)
    output3 = cmd_out3.communicate()[0].decode('utf-8')
    print(output3)
    # Open the File
    gpsfile = open("/home/john/CAPSTONE/Data%s.txt"%str(i), "r")
    # Grab the Data
    print('Opened the File!\n')
    # Close the File
    gpsfile.close()

