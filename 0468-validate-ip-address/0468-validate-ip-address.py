class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        validletters = {'a':1,'b':1,'c':1,'d':1,'e':1,'f':1,"A":1,"B":1,"C":1,"D":1,"E":1,"F":1}

        def isvfour(query):
            for item in query:
                if not item:
                    return False
                for val in item:
                    if val.isdigit():
                        continue
                    else:
                        return False
                if int(item) <0 or int(item)>255:
                    return False

                if len(item)>1:
                    print(item[0])
                    if item[0]=="0":
                        return False
            return True
        
        def isvsix(query):
        
            for item in query:
                if len(item)<1 or len(item)>4:
                    return False
                
                for val in item:
                    if val.isdigit():
                        continue
                    if val not in validletters:
                        print(val)
                        return False
            return True

        if '.' in queryIP:
            query = queryIP.split(".")
        else:
            query = queryIP.split(":")
        if len(query)==4 and isvfour(query):
            return "IPv4"
        elif len(query)==8 and isvsix(query):
            return "IPv6"
        else:
            return "Neither"
        