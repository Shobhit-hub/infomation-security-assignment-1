'''
Output
Enter a string to encode : Shobhit@21
Encoded String :  38 401 111 89 401 501 611 @ owt eno 
'''
#Program for Additive Cypher

#function to encode 
def encode(text,shift):
    result=""
    for i in range(0,len(text)):
        if text[i]>='a' and text[i]<='z':
            result+=chr(((ord(text[i])-ord('a')+shift)%26)+ord('a'))
        elif text[i]>='A' and text[i]<='Z':
            result+=chr(((ord(text[i])-ord('A')+shift)%26)+ord('A'))
        else:
            result+=text[i]
    return result
#function to decode
def decode(text,shift):
    result=""
    for i in range(0,len(text)):
        if text[i]>='a' and text[i]<='z':
            result+=chr(((ord(text[i])-ord('a')-shift)%26)+ord('a'))
        elif text[i]>='A' and text[i]<='Z':
            result+=chr(((ord(text[i])-ord('A')-shift)%26)+ord('A'))
        else:
            result+=text[i]
    return result       

def main():
    while True:
        print("MENU")
        print("1.Encode")
        print("2.Decode")
        print("3.Exit")
        while True:
            try:
                choice=int(input('Enter choice: '))            
                if choice <1 or choice >3:
                    print("Input not in range 1-3 !! Try Again")
                    continue
                break
            except:
                print("Invalid Choice")
        if choice<3:
            text=input("Enter a string : ")  #Input string
            while True:
                try:
                    shift=int(input('Enter shift: '))            #input shift 
                    break
                except:
                    print("Please enter a number")
        if choice==1:
            print("Encoded String : ",encode(text,shift))
        elif choice==2:
            print("Decoded String : ",decode(text,shift))
        else:
            break
                
main()
        
    
