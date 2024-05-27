# ZKTeco Insecure Direct Object Reference (IDOR) 

This Python script is designed to exploit an IDOR vulnerability in some ZKTeco devices.
There are URLs that can be accessed without any authentication, only the IP of the device is required and you can open the door or reboot the device.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/hernandocastelli/zkteco.git
    ```

2. Navigate to the project directory:

    ```bash
    cd zkteco
    ```

3. Install the required Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

    Usage:
        python zkteco.py [options] <ip>

    Options:
        -o, --open       Open the door
        -r, --reboot     Reboot device

    Arguments:
        ip               Device IP address

## License

This project is licensed under the MIT License.
