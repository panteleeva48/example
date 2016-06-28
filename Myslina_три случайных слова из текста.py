import random

def openfile (name):
    f = open(name,'r', encoding = 'UTF-8')
    s = f.read()
    f.close()
    return s

def cleansplit (s):
    s = s.replace('\n', ' ')
    s = s.lower()
    txt = s.split(' ')
    txt = list (txt)
    
    for indx, word in enumerate (txt):
        word = word.strip('.,?!/;:"()[]{}\n\r-«»')
        txt[indx] = word
    return txt
#print (cleansplit (openfile ('vojd.txt')))
#def main():
arr = cleansplit(openfile('vojd.txt'))
print (random.choice(arr))
print (random.choice(arr))
print (random.choice(arr))
    
#if  __name__ == '__main__':
#    main()
