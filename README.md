### What is My Wi-Fi Password
    This program is used to find the Wi-Fi name (SSID) and password (key) of all 
    networks you have connected to. The results will be saved to a text file where 
    it can be viewed.

### Usage
    git clone https://github.com/dk2684/What-is-My-WiFi-Password.git
    cd What-is-My-WiFi-Password
    python get_passwords.py (Saves information to a text file in the same directory)
    OR
    python print_passwords.py (Prints information to standard output)
    
### Example Output
    Wi-Fi Name (SSID)             | Password
    ----------------------------------------------
    Home-Network                  | Password123
    
### Options
    N/A
    
### Notes
    Supported Operating Systems: Windows 7 or above.
    OS Language must be in English because string comparisons are used.
    Networks with special types of authentications (e.g. enterprise) cannot be revealed through command prompt.    
