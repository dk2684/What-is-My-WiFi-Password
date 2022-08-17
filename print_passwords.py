# import module to create new process
import subprocess

# list of profiles that will hold network SSIDs
profiles = []

# getting raw output data
output_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

# decoding and splitting the raw data
data = output_data.decode('utf-8', errors ="backslashreplace")
data = data.split('\n')

# loops through data for connected networks
for i in data:

    if "All User Profile" in i:

        # Splits the item if found
        i = i.split(":")

        # Network SSID is in Index 1
        i = i[1]

        # Removes quotations from SSID name
        i = i[1:-1]

        # Adds Network SSID to profiles list
        profiles.append(i)


# print formatted heading    
print("{:<30}| {:<}".format("Wi-Fi Name (SSID)", "Password"))
print("----------------------------------------------")

# loops through list of profiles
for i in profiles:
    
    try:
        # getting raw output data (using network SSID)
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear'])
        
        # decoding and splitting the raw data
        results = results.decode('utf-8', errors ="backslashreplace")
        results = results.split('\n')
        
        # looping through each row in results data
        for row in results:
            # locating network key
            if "Key Content" in row:
                # removes excess characters and saves only network key
                results = [row.split(":")[1][1:-1]]

        # if key exists: prints SSID key
        try:
            print("{:<30}| {:<}".format(i, results[0]))
            
        # else: prints blank key, in cases such as key content not being available
        except IndexError:
            print("{:<30}| {:<}".format(i, ""))
                
        
                
    # exception if process fails or throws error
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "Encoding Error Occurred"))
