def lengthOfLongestSubstring(s):
    """
    Given a substring s, find the length of the longest substring without repeating characters.
    input substring s numbers, spaces,letters
    output kongest substring
    """
    #to store the substring
    substring="" 
    # the length of substring
    longest=0
    # starts if the input length > 1
    if len(s) > 1:
        # to loop over the input substring
        for char in s:
            # adding chars only if the substring variable does have it
            if (char not in substring):

                substring=substring+char  #concatenate chars to form substring
                #check if the formed substring == len of input then returns the length
                # ex: if user entered abc then the formed substring is abc 
                if len(substring) == len(s) and len(substring) > longest:
                    return len(substring)
            # if the char in trun in substring
            else:
                    if longest ==0 or len(substring) >= longest:
                        longest = len(substring)
                    """
                    to find the position of the first char in the substring and removes it and anything before it
                    also removes the substring from the main substring (the input)
                    ex1 abcanf result >> bcanf 
                    ex2 lsasam result >> sam
                    """
                    pos=substring.find(char)+1
                    st=substring[:pos]
                    s=s.replace(st,'',1)
                    substring=substring.replace(substring[:pos],"",1)+char
                    st=""
                    pos=0        
        return longest
    # if the input length <= 1 to deal with empty and one-char input 
    else:
        return len(s)

test_cases= { "": 0," " : 1,"c" :1,"aab":2,"dvdf":3,"tmmzuxt":5,
"asljlj":4,"ohvhjdml":6,"loddktdji":5,"ggububgvfk":6,"pwwkew" :3,"abcabcbb":3,"bbbbb":1}

def test():
    for key,value in test_cases.items():
        try:
            assert lengthOfLongestSubstring(key)==value
            output=lengthOfLongestSubstring(key)
            print("case {} passed! expected {} output {}".format(key,value,output))
        except:
            output=lengthOfLongestSubstring(key)
            print("case {} failed! expected {} but output {}".format(key,value,output))
test()
            
            
                
                
                
                
                
                
                
                
                
                
                
                
                



    

