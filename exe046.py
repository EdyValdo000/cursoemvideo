from time import sleep
import emoji
for n in range(10,-1,-1):
    print(n)
    sleep(1)
print(emoji.emojize('\033[1;32mFeliz ano novo! :star-struck:\033[m'))