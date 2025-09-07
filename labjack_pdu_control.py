import time
import numpy as np
from datetime import datetime
from labjack import ljm


RED = '\033[1;31m'
GREEN = '\033[1;32m'
RESET = '\033[0;0m'

""" Connect to Labjack """
handlelab2 = ljm.openS("T4", "USB", "470035783")


def relay_status():
    global relay_state
    global no_b
    relay_state = bin(int(ljm.eReadName(handlelab2, "DIO_STATE")))
    # 0b10000
    no_b = relay_state[2:].zfill(12)[0:12][::-1]
    # 000000010000
    # 000010000000
    relay_one_status = f"Relay 1 {GREEN}On!{RESET}" if (no_b[4] == '1') else f"Relay 1 {RED}Off!{RESET}"

    relay_two_status = f"Relay 2 {GREEN}On!{RESET}" if (no_b[5] == '1') else f"Relay 2 {RED}Off!{RESET}"

    relay_three_status = f"Relay 3 {GREEN}On!{RESET}" if (no_b[6] == '1') else f"Relay 3 {RED}Off!{RESET}"

    relay_four_status = f"Relay 4 {GREEN}On!{RESET}" if (no_b[7] == '1') else f"Relay 4 {RED}Off!{RESET}"

    relay_five_status = f"Relay 5 {GREEN}On!{RESET}" if (no_b[8] == '1') else f"Relay 5 {RED}Off!{RESET}"

    relay_six_status = f"Relay 6 {GREEN}On!{RESET}" if (no_b[9] == '1') else f"Relay 6 {RED}Off!{RESET}"

    relay_seven_status = f"Relay 7 {GREEN}On!{RESET}" if (no_b[10] == '1') else f"Relay 7 {RED}Off!{RESET}"

    relay_eight_status = f"Relay 8 {GREEN}On!{RESET}" if (no_b[11] == '1') else f"Relay 8 {RED}Off!{RESET}"

    print("\n------------------------------------------------------")

    print(f"{relay_one_status} | {relay_two_status} | {relay_three_status} | {relay_four_status} | {relay_five_status} | {relay_six_status} | {relay_seven_status} | {relay_eight_status}")


if __name__ == '__main__':
    # Relays will always be commanded on by the controller
    ljm.eWriteName(handlelab2, 'DIO4', 1)
    ljm.eWriteName(handlelab2, 'DIO5', 1)
    ljm.eWriteName(handlelab2, 'DIO6', 1)
    ljm.eWriteName(handlelab2, 'DIO7', 1)
    ljm.eWriteName(handlelab2, 'DIO8', 1)
    ljm.eWriteName(handlelab2, 'DIO9', 1)
    ljm.eWriteName(handlelab2, 'DIO10', 1)
    ljm.eWriteName(handlelab2, 'DIO11', 1)


    while True:
        relay_status()
        print(f"1. Box 1 Relay 1\n2. Box 1 Relay 2\n3. Box 1 Relay 3\n4. Box 1 Relay 4\n0. Exit")
        user_input = input("Enter a Number: ")
        print("------------------------------------------------------")
        choice = int(user_input)
        if choice == 1:
            if no_b[0] == "1":
                ljm.eWriteName(handlelab2, 'DIO4', 0)
            else:
                ljm.eWriteName(handlelab2, 'DIO4', 1)
        if choice == 2:
            if no_b[1] == "1":
                ljm.eWriteName(handlelab2, 'DIO5', 0)
            else:
                ljm.eWriteName(handlelab2, 'DIO5', 1)
        if choice == 3:
            if no_b[2] == "1":
                ljm.eWriteName(handlelab2, 'DIO6', 0)
            else:
                ljm.eWriteName(handlelab2, 'DIO6', 1)
        if choice == 4:
            if no_b[3] == "1":
                ljm.eWriteName(handlelab2, 'DIO7', 0)
            else:
                ljm.eWriteName(handlelab2, 'DIO7', 1)
        if choice == 5:
            if no_b[0] == "1":
                ljm.eWriteName(handlelab2, 'DIO8', 0)
            else:
                ljm.eWriteName(handlelab2, 'DIO8', 1)
        if choice == 6:
            if no_b[1] == "1":
                ljm.eWriteName(handlelab2, 'DIO9', 0)
            else:
                ljm.eWriteName(handlelab2, 'DIO9', 1)
        if choice == 7:
            if no_b[2] == "1":
                ljm.eWriteName(handlelab2, 'DIO10', 0)
            else:
                ljm.eWriteName(handlelab2, 'DIO10', 1)
        if choice == 8:
            if no_b[3] == "1":
                ljm.eWriteName(handlelab2, 'DIO11', 0)
            else:
                ljm.eWriteName(handlelab2, 'DIO11', 1)
        elif choice == 0:
            ljm.close(handlelab2)
            exit()


    ljm.close(handlelab2) # Close connection to Labjack2