import ast
real_data = open("/home/john/CAPSTONE/filtered_data_file.txt", "w")
for i in (1, 2, 3):
    gpsfile = open("/home/john/CAPSTONE/Data%s.txt"%str(i), "r")
    # Grab the Data
    line0 = gpsfile.readline()
    true_data = line0.split(',')
    real_data.write(true_data[1]+ ' ' + true_data[2]+"\n")
    real_data.write(true_data[3] + ' ' +  true_data[4] + "\n")
    # Close the File
    gpsfile.close()
real_data.close()  # don't want to continue writing to this file after this
fun_data = open("/home/john/CAPSTONE/filtered_data_file.txt", "r")  # just reading from file now
latitude = [0, 0, 0]
longitude = [0, 0, 0]
count_long = 0
count_lat = 0
for i in (0,1,2,3,4,5):
    line1 = fun_data.readline()
    split = line1.split()
    number = float(split[0])
    print(number)
    if i%2 == 0:
        degree = float(str(number)[:2])
        minute = float(str(number)[2:])/60.0
        latitude[count_lat] = degree + minute
        count_lat = count_lat + 1
    else:
        degree = float(str(number)[:4])
        minute = float(str(number)[4:])/60.0
        longitude[count_long] = degree - minute
        count_long = count_long + 1
print(latitude)
print(longitude)
# Closing the file
fun_data.close()
# Setting the motors in a certain position
# exec(open("/home/john/CAPSTONE/Motor_Control_Software_Acceptance_Test.py").read())
with open("/home/john/CAPSTONE/Dist_File.txt") as data:
    dist_dictionary = ast.literal_eval(data.read())

# Convert feet to decimal degrees
conversion_factor = 90/(10000*3280.84)
SSID1 = dist_dictionary['SSID1']*conversion_factor
SSID2 = dist_dictionary['SSID2']*conversion_factor
SSID3 = dist_dictionary['SSID3']*conversion_factor
print(SSID1)
print(SSID2)
print(SSID3)
a = latitude[0]
c = latitude[1]
f = latitude[2]
b = longitude[0]
d = longitude[1]
g = longitude[2]
print(a)
print(c)
print(f)
print(b)
print(d)
print(g)
# f^2 + g^2 - r3^2 - a^2 -b^2 + r1^2
alpha = (f ** 2) + (g ** 2) - (SSID3 ** 2) - (a ** 2) - (b ** 2) + (SSID1 ** 2)
# c^2 + d^2 - r2^2 - a^2 -b^2 + r1^2
beta = (c ** 2) + (d ** 2) - (SSID2 ** 2) - (a ** 2) - (b ** 2) + (SSID1 ** 2)
# -b+g
zeta = -b+g
# -b+d
gamma = -b+d

x_location = ((alpha/(2*zeta))-(beta/(2*gamma))) / (((a-c)/gamma)-((a-f)/zeta))  # x-coordinate of the intersection of three circles
y_location = (((a-c)*x_location)/gamma)+((beta)/(2*gamma))  # y-coordinate of the intersection of three circles
print(x_location)
print(y_location)
