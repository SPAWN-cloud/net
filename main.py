# first we will import the subprocess module
import subprocess

#now we will store the profiles data in "data" variable by
# running the 1st cad command using subprocess. check output
data = subprocess.check_output ( [netsh', 'wlan", "show', 'profiles
})

.decode(utf-8).split( \n" )

#now we will store the profile by converting them to list
profiles [1.split(": ")[1][1:-1] for in data if "All User Profile" in

#Using for Loop in python we are checking and printing the wift
#passwords if they are available using the 2nd cmd command
for i in profiles:

#running the 2nd cnd command to check passwords

results = subprocess .check output ( ["netsh', 'wlan', 'show",

"profile', 1,

"key=clear 1).decode( utf-8').split( '\n?)

#storing passwords after converting them to list
results [b.split(": [1][1:-1] for b in results if "Key Content"

in bl

#printing the profiles (wift name) with their passwords using
#try and except method

try:

print ("(:<38}|

except IndexError :

print ("(:<30)|

().format( 1, results [0] ))

(:<)".format((, ""))
