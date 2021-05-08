from PyDictionary import PyDictionary
dict = PyDictionary()
def meaning(word):
    meaning = str(dict.meaning(word))
    
    try:
        result = meaning.split(":")
        result = result[1].split(",")
        temp = result = result[0][3:]
        
    except Exception as e:
        result = "Sorry sir, Not Found"
    return str(result)