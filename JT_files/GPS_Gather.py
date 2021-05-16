def read_GPS():
    from machine import UART
    import time
    uart = UART(2, 9600)  # sets the UART pins
    time.sleep(5)  # sleep for 5 seconds, letting data accumulate
    input_data = uart.readline()
    write_data1 = input_data.decode()
    key = '$GPGLL'
    while key not in write_data1:
        # This keeps checking the input until the correct GPS sentence is found
        time.sleep(1)  # sleep for one second, letting data accumulate
        input_data = uart.readline()
        write_data1 = input_data.decode()

    end_index = write_data1.find('\\r')  # Finds where the $GPGLL sentence ends
    write_data2 = write_data1[:end_index]  # Extracts the sentence
    file1 = open('data.txt', 'a')  # Appending the data.txt file
    file1.write(write_data2)  # Writes the GPS Sentence into the file
    file1.close()  # Closes the file




