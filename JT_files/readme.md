
GPS_DATA_ACCEPTANCE_TEST file contains code that allows GPS data to be read from ESP32 Module by switching the current wifi station the Jetson is listening to and then opening a WebRepl console to guide the transfer of data

Localization_Algorithm file contains the code that takes the GPS data and the code from Erik's relative distance calculation to calculate the absolute position of the Jetson

Motor_Control file contains code to control the PCA9685 breakout board, change the angle of the motors, and report that angle back. This in combination with code from Servomotor_Acceptance will allow full control over the angle of the motor.

Servomotor_Acceptance contains code to control the angles of the motors attached to hte PCA9685 breakout board.

The .sh files are script files to force the Jetson to change which Wi-Fi station it is listening to.
