# Window Manager Scripts (for Hyprland)
The applications/scripts in this repo are designed for Hyprland in mind, any external application is noted in the below README.
<br><br>

## Mako Sudo Checker v1.0.0
### Overview

**Mako Sudo Checker** is a Python script designed to monitor the presence of active `sudo` processes and send urgent desktop notifications when a sudo password is required. This tool is particularly useful for system administrators and developers who need to be promptly alerted to sudo activities on their system. This script is designed with Hyprland and Mako in mind.

### Features

- Monitors for active `sudo` processes.
- Sends an urgent desktop notification using `notify-send` when a sudo password is required.
- Dismisses existing notifications before sending a new one.
- Clears the terminal screen for updated notifications.

### Requirements

- Python 3
- `pidof` command
- `makoctl` for notification management
- `notify-send` for sending desktop notifications

### Usage

1. Make the script executable:
    ```sh
    chmod +x mako_sudo_checker.py
    ```

2. Run the script:
    ```sh
    ./mako_sudo_checker.py
    ```

The script will continuously monitor for `sudo` processes and send notifications as configured.

## Adding to Startup

To ensure the script runs at startup, add it to your window manager or desktop environment's startup script. This script is designed with Hyprland and Mako in mind, but it can be adapted for other environments.

For example, in Hyprland, you might add the following line to your `hyprland.conf`:

```sh
exec --no-startup-id /path/to/mako_sudo_checker.py
```

Adjust the path to point to the location of your `mako_sudo_checker.py` script.

## Customization

To customize the notification icon, ensure your desired icon image is named `siren.png` and placed in the same directory as the script. You can also modify the notification message within the `send_urgent_notification` function.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify the content to better suit your specific repository and requirements.
