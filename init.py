import sys
import requests
import os
from dotenv import load_dotenv

load_dotenv()
day = int(sys.argv[1])
path = f"./{day:02d}"

USER_AGENT = "https://github.com/tytot/advent-of-code-2022 by @tytot on Github"
URL = f"https://adventofcode.com/2022/day/{day}/input"
cookie = os.getenv('COOKIE')

# create folder for day
if not os.path.exists(path):
    os.makedirs(path)

# attempt to fetch inputs
if not os.path.exists(f"{path}/input.txt"):
    try:
        with requests.get(url=URL, cookies={"session": cookie}, headers={"User-Agent": USER_AGENT}) as response:
            if response.ok:
                data = response.text
                input = open(f"{path}/input.txt", "w+")
                input.write(data.rstrip("\n"))
                input.close()
            else:
                print("Server response sus")
    except Exception as e:
        print("Something went wrong lol")

# try to set up code
if not os.path.exists(f"{path}/solution.py"):
    code = open(f"{path}/solution.py", "w+")
    code.write(
        f"input = open(__file__.rstrip('solution.py') + 'input.txt').read()")
    code.close()
