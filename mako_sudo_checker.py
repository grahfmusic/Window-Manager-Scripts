#!/usr/bin/python3
import subprocess
import time
import os

def print_header():
    print("\033[\n1;34m.: Make Sudo Checker v1.0.0 :.")
    print("\033[1;34m.:        2024  Grahf       :.")
    print("\033[0m\n")

def get_sudo_pid():
    result = subprocess.run(["pidof", "sudo"], capture_output=True, text=True)
    return result.stdout.strip()

def get_mako_notifications():
    result = subprocess.run(["makoctl", "list"], capture_output=True, text=True)
    return result.stdout

def dismiss_mako_notifications():
    subprocess.run(["makoctl", "dismiss"])

def send_urgent_notification(image_path):
    subprocess.run([
        "notify-send", "URGENT", "Password Required For Sudo",
        "-i", image_path, "-u", "critical"
    ])

def clear_screen():
    print("\033[0J", end='')  # Clear from cursor to the end of the screen

def get_command_from_pid(pid):
    try:
        result = subprocess.run(["ps", "-p", pid, "-o", "comm="], capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return ""

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "siren.png")

    print_header()

    last_sudo_pid = ""
    last_output_sudo = ""
    last_output_notification = ""
    notification_state = ""

    # List of process names to be excluded from notifications
    exceptions = ["ccavpn", "openvpn"]

    while True:
        sudo_pid = get_sudo_pid()

        if sudo_pid:
            command = get_command_from_pid(sudo_pid)
            if command in exceptions:
                time.sleep(1)
                continue

            if sudo_pid != last_sudo_pid:
                clear_screen()
                last_output_sudo = ""
                last_output_notification = ""
                last_sudo_pid = sudo_pid

            sudo_state = f"\033[0;36m :: PID with sudo: \033[1;31m{sudo_pid}"

            mako_notifications = get_mako_notifications()
            if "URGENT" not in mako_notifications:
                dismiss_mako_notifications()
                send_urgent_notification(image_path)
                notification_state = " :: Notification Sent"

            if sudo_state != last_output_sudo:
                print(f"\033[0K\r{sudo_state}", end='', flush=True)
                last_output_sudo = sudo_state

            if notification_state != last_output_notification:
                print(f"\n\033[0K{notification_state}", end='', flush=True)
                last_output_notification = notification_state

        else:
            if last_output_sudo or last_output_notification:
                clear_screen()
                last_output_sudo = ""
                last_output_notification = ""
                last_sudo_pid = ""

        time.sleep(1)

if __name__ == "__main__":
    main()
