from time import sleep
from random import shuffle
from os import system
import colorama,re
colorama.init(autoreset=True)
clear = lambda: system("cls")
clear()
print('\n     COMBO EDITOR V1       By https://www.instagram.com/a7.acc \n')
print('''
🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
🟥🟥⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜
🟥🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
🟥🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
              @A7.acc
''')

file = input('Enter the combo file name >> ')
if not file.endswith('.txt'):
    file = file+'.txt'

combo = []
try:
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            combo.append(line.strip('\n'))
except Exception as error:
    print('[!] Error while openning '+file+' !')
    print('Error message >> '+str(error))
    sleep(7)
    exit()

def ask():
    choice = input('''\n   Choose an option:
[1] Combo Slicer               (slices from line to another with randomize)
[2] Combo Slicer               (slices from line to another without randomize)
[3] Combo Cleaner              (removes bad, empty and dublicated lines for E:P combos)
[4] Dublicate Remover          (with randomizing)
[5] Custom domain              (@yahoo only - @gmail only ...)
[6] Combo Seperator            (keep mails, passwords, IP\'s or phone numbers only)
[7] Combo Flipper              (flip for example from E:P to P:E)
[8] Custom                     (choose lines with certain regex)
[9] Exit
        >>  ''')
    return choice

while True:
    choice = ask()
    if choice == '1':
        fromy = int(input('FROM which line do you want to start? >>  '))
        if fromy == '0':
            fromy = '1'
        too = int(input('TO which line? >> '))
        lines = []
        i = 0
        for line in combo:
            if int(fromy) <= i <= int(too):
                print(i)
                lines.append(line)
            i += 1

        for _ in range(10):
            shuffle(lines)

        with open(file,'w',encoding='utf-8') as file:
            for i in lines:
                file.write(i.strip('\n')+'\n')

        print('Done slicing the combo from '+str(fromy)+' till '+str(too)+' and randomize it')
        print('There is '+str(len(lines))+' line currently in the file')
        sleep(5)
        clear()

    elif choice == '2':
        fromy = int(input('FROM which line do you want to start? >>  '))
        if fromy == '0':
            fromy = '1'
        too = int(input('TO which line? >> '))
        lines = []
        i = 0
        for line in combo:
            if int(fromy) <= i <= int(too):
                lines.append(line)
            i += 1

        with open(file,'w',encoding='utf-8') as file:
            for i in lines:
                file.write(i.strip('\n')+'\n')

        print('Done slicing the combo from '+str(fromy)+' till '+str(too))
        print('There is '+str(len(lines))+' line currently in the file')
        sleep(5)
        clear()

    elif choice == '3':
        clean = set()
        for com in combo:
            try:
                com = com.split(':')
            except:
                pass
            try:
                if '@' in com[0] and '.' in com[0]:
                    if len(com) == 2:
                        com = com[0]+':'+com[1]
                        clean.add(com)
            except:
                pass
        
        clean = list(clean)
        with open(file,'w',encoding='utf-8') as file:
            for i in clean:
                file.write(i.strip('\n')+'\n')

        print('Done cleaning the combo!')
        print('There is '+str(len(clean))+' line currently in the file')
        sleep(5)
        clear()
    
    elif choice == '4':
        como = set()
        for com in combo:
            como.add(com)

        como = list(como)
        with open(file,'w',encoding='utf-8') as file:
            for i in como:
                file.write(i.strip('\n')+'\n')

        print('Done removing dublicated lines and randomizing the combo!')
        print('There is '+str(len(como))+' line currently in the file')
        sleep(5)
        clear()

    elif choice == '5':
        cho = input('Enter a domain to keep (if more than one seperate them by a space like this > @gmail @yahoo ...) >>> ')
        while True:
            comby = input('Do you want the emails only?? (y/n) >> ').lower()
            if comby == 'y':
                ans = input('Your combo passwords are going to get deleted. Are you sure that you want to continue? (y/n) >> ')
                if ans == 'y':
                    break
            elif comby == 'n':
                break
            
        domains = cho.split(' ')
        keep = set()
        for com in combo:
            try:
                com = com.split(':')
                for domain in domains:
                    if domain in com[0]:
                        if comby == 'y':
                            keep.add(com[0])
                        else:
                            keep.add(com[0]+':'+com[1])
            except:
                pass

        keep = list(keep)
        with open(file,'w',encoding='utf-8') as file:
            for i in keep:
                file.write(i.strip('\n')+'\n')

        print('Done keeping certain domains only!')
        print('There is '+str(len(keep))+' line currently in the file')
        sleep(5)
        clear()
    
    elif choice == '6':
        ans = input('''What do you want to keep? 
[1] Mails
[2] Passwords
[3] IP\'s
[4] Phone numbers
[5] Exit
    >> ''')
        output = set()
        for com in combo:
            if ans == '1':
                keepy = 'Mails'
                com = com.split(':')
                for co in com:
                    out = re.findall(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",co)
                    if len(out) == 1:
                        output.add(out[0])
            elif ans == '2':
                keepy = 'Passwords'
                so = com.split(':')
                for i in so:
                    if len(re.findall(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",i)) == 0 and len(re.findall(r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}',i)) == 0 and len(re.findall(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',i)) == 0:
                        if '@' not in i or '.' not in i:
                            output.add(i)
            elif ans == '3':
                keepy = 'IP\'s'
                com = com.split(':')
                com = ''.join(com)
                ip = re.findall(r'[0-9]{,3}\.[0-9]{,3}\.[0-9]{,3}\.[0-9]{,3}',com)
                if len(ip) == 1:
                    output.add(ip[0])
            elif ans == '4':
                keepy = 'Phone numbers'
                phone = re.findall(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',com)
                if len(phone) == 1:
                    output.add(phone[0])
            else:
                break
        if ans != '5':
            output = list(output)
            try:
                with open(file,'w',encoding='utf-8') as file:
                    for i in output:
                        file.write(str(i).strip('\n')+'\n')
            except:
                with open(file,'w') as file:
                    for i in output:
                        file.write(i.strip('\n')+'\n')


            print('Done keeping all '+str(keepy)+' !!')
            print('There is '+str(len(output))+' line currently in the file')
            sleep(5)
            clear()
    elif choice == '7':
        seperator = input('Enter your seperator (in default \':\' is the seperator ) >> ')
        new = []
        for com in combo:
            if seperator == '' or seperator == ':':
                com = com.split(':')
                try:
                    new.append(str(com[1]+':'+com[0]))
                except:
                    pass
            else:
                com = com.split(seperator)
                try:
                    new.append(com[1]+seperator+com[0])
                except:
                    pass
    
        fv =  open(file,'w',encoding='utf-8')
        for i in new:
            fv.write(str(i).strip('\n')+'\n')
        fv.close()

        print('Done flipping the combo !!')
        print('There is '+str(len(new))+' line currently in the file')
        sleep(5)
        clear()


    elif choice == '8':
        reg = input('Enter your regex >> ')
        regy = []
        for com in combo:
            try:
                f = re.findall(reg,com)
                if len(f) > 0:
                    regy.append(f[0])
            except:
                pass
        
        output = regy
        with open(file,'w',encoding='utf-8') as file:
            for i in output:
                file.write(str(i).strip('\n')+'\n')
        
        print('Done keeping all items with '+str(reg)+' regex!!')
        print('There is '+str(len(output))+' line currently in the file')
        sleep(5)
        clear()

    else:
        print('BYE! :)')
        sleep(5)
        break



            


            
        




