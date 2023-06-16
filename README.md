# USB-blocker
## **Project Description: USB Port Control**

The "USB Port Control" project is a Python script that provides functionality to check, block, and unblock USB ports on a Windows system. This project aims to offer users control over the USB ports' accessibility, allowing them to enhance security measures or manage device connectivity.

The script utilizes the Windows registry to interact with the USB storage service (USBSTOR) and retrieve or modify the port status. It employs the os and re modules to execute registry queries and handle regular expressions for extracting relevant information.
## **Installation**

1. Clone the repository or download the script file (usb_port_control.py) to your local machine.
2. Ensure that you have Python 3.x installed on your system.
3. Open a command-line interface (e.g., Command Prompt, Terminal).
4. Navigate to the directory where the script is located using the cd command.
5. Install the required modules by executing the following command:

```
pip install regex
```
6. Once the installation is complete, you are ready to use the "USB Port Control" script.


## **Usage**

1. Open a command-line interface (e.g., Command Prompt, Terminal).
2. Navigate to the directory where the script (usb_port_control.py) is located using the cd command.
3. Run the script by executing the following command:

```
python usb_port_control.py
```

4. The script will display the current status of the USB ports, indicating whether they are blocked or unblocked.
5. You will be prompted with the following message:

```
Do you want to block or unblock USB ports? [block/unblock]:
```

6. Enter your choice by typing either "block" or "unblock" (without quotes) and press Enter.
7. Depending on your selection and the current status of the USB ports, the script will perform the requested action and display an appropriate success or failure message.
8. After the action is completed, the script will prompt you to press Enter to continue.

This "USB Port Control" project can be useful in scenarios where controlling USB port accessibility is desired, such as in public computer systems, corporate environments, or systems with strict security policies. By blocking USB ports, unauthorized data transfer or introduction of potentially harmful devices can be prevented, enhancing overall system security.

The script can be integrated into larger systems or used independently, offering a convenient way to manage USB port control programmatically. It serves as a practical 
