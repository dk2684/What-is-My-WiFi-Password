# import module to create new process
import subprocess

# list of profiles that will hold network SSIDs
profiles = []

# text that will be saved to .txt file
output = ""

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


# inputs formatted heading    
output += "{:<30}| {:<}\n".format("Wi-Fi Name (SSID)", "Password")
output += ("----------------------------------------------\n")

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

        # if key exists: inputs SSID key
        try:
            output += "{:<30}| {:<}\n".format(i, results[0])
            
        # else: inputs blank key, in cases such as key content not being available
        except IndexError:
            output += "{:<30}| {:<}\n".format(i, "")
                
        
                
    # exception if process fails or throws error
    except subprocess.CalledProcessError:
        output +=  "{:<30}|  {:<}\n".format(i, "Encoding Error Occurred")

# duplicate files will be overwritten, otherwise new .txt file will be created
with open('./network_passwords.txt', 'w') as file:
    file.write(output)

# print success message to standard output
print("Process complete. Network information has been saved to \"network_passwords.txt\" in this directory.")
