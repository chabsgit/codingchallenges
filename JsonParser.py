

'''
Version 1: Only Validates if json string starts 
with curly brackets or not
'''
# Version1
def validateJson(jsonStr):
    if jsonStr.startswith("{") and jsonStr.endswith("}"):
        return True
    else:
        return False
    

# Version2
'''
its only for {"key""value"}

'''
def validateJson_ver2(jsonStr):
    if(validateJson(jsonStr)):
        stack = []
        temp = jsonStr
        temp = temp.replace("{","")
        temp = temp.replace("}","")
        for i in jsonStr:
            if i == '"':
                if len(stack)==0:
                    stack.extend(i)
                else:
                    stack.pop()
        
        if len(stack)==0:
            return True
        else:
            return False
            
    else:
        return False
        

# Version2
'''
its only for {"key""value"}
'''

class JsonParserVer3:
    def __init__(self,jsonStr) -> None:
        self.jsonStr = jsonStr
        self.charIndex = 0
        self.jsonDict = self.parse()
        

    def parse(self):
        self.jsonStr.strip()
        
        if not (self.jsonStr.startswith("{") and self.jsonStr.endswith("}")):
            return None
        tempdict = {}
        
        self.charIndex += 1 #to skip {
        while self.jsonStr[self.charIndex] != "}":
            self.removeWhiteSpace()
            key = self.readKey()
            self.removeWhiteSpace()
            ch = self.jsonStr[self.charIndex]
            if ch != ":":
                print(": is expected")
                break
            
            self.charIndex += 1
            self.removeWhiteSpace()
            ch = self.jsonStr[self.charIndex]
            value = None
            
            if ch == '[':
                value = self.readList()
            elif ch == '{':
                value = self.parse()
            else:
                value = self.parseValue()
            tempdict[key] = value
        return tempdict
    
    def readString(self):
        self.charIndex += 1
        start = self.charIndex
        while self.jsonStr[self.charIndex] != '"':
            self.charIndex += 1
        str = self.jsonStr[start:self.charIndex]
        self.charIndex += 1 # to skip closing double quote
        return str
    
    def readNumber(self):
        pass
        
    def readKey(self):
        self.charIndex += 1
        start = self.charIndex
        while self.jsonStr[self.charIndex] != ':':
            self.charIndex += 1
        key = self.jsonStr[start:self.charIndex].replace('"','').replace(" ",'')
        return key
    
    def parseValue(self):
        start = self.charIndex
        while not(self.jsonStr[self.charIndex] == ',' or self.jsonStr[self.charIndex] == '}'):
        # while self.jsonStr[self.charIndex] != '"':
            self.charIndex += 1
        value = self.jsonStr[start:self.charIndex].strip()
        
        if value.startswith('"'):
            value = self.jsonStr[start:self.charIndex].replace('"','')
        elif value.lower() == 'true' or value.lower() == 'false':
            value = bool(value)
        elif value[0].isdigit() or value[0] == "-":
            value = int(value)
        elif value.lower() == 'null':
            value = None
        else:
            print("Invalid value:" + value)
        
        return value    
    
    def removeWhiteSpace(self):
        ch = self.jsonStr[self.charIndex].strip()
        while ch == '':
            self.charIndex += 1
            ch = self.jsonStr[self.charIndex].strip()
    
    def readList(self):
        jsonlist = []
        start = self.charIndex + 1 # to remove [ 
        ch = self.jsonStr[self.charIndex].strip()
        while ch != ']':
            self.charIndex += 1
            ch = self.jsonStr[self.charIndex].strip()
        jsonlist = self.jsonStr[start:self.charIndex].split(",")
        self.charIndex += 1 # to remove ]
        return jsonlist
    


str = '{"name":"John","city":"New York", "color":"yellow"}'
str1 = '{"booly": true, "name":"John", "numm" : 123 , "nonny" : null, "name" : "Aparna", "list1":[1,2,3]}'
str2 = '{"name":"John",  "city":"New York", "list1":[1,2,3] , "items":{"name1": "chabu"}}'

js = JsonParserVer3(str2)
print(js.jsonDict["list1"][0])


