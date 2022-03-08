import pafy
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

pafy.set_api_key(API_KEY)

url = 'https://www.youtube.com/watch?v=0uAxgTkr6pI'

get = pafy.new(url)

save = get.getbest()




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    save = get.getbest()
    save.download()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
