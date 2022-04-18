
def romanToInt(text):
    dictionary={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    text=text.upper()
    sum_=[]
    i=0
    if 1 <=len(text) <= 15:
        while(i+1 < len(text)):
            if dictionary[text[i]] >= dictionary[text[i+1]]:
                sum_.append(dictionary[text[i]])
                text=text.replace(text[i],'',1)
            else :
                sum_.append(dictionary[text[i+1]]-dictionary[text[i]])
                text=text.replace(text[i:i+2],'',1)  
        if len(text)==1:
            sum_.append(dictionary[text])
    else:
        return "Invaild input"
    return sum(sum_)

print(romanToInt("iv"))
