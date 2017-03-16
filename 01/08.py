def cipher(doc):
    new_doc = ""
    for i in range(len(doc)):
        if doc[i].islower():
            new_doc = new_doc + chr(219-ord(doc[i]))
        else:
            new_doc = new_doc + doc[i]
    
    return new_doc

doc = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

print("origin text: %s"%doc)
print("cipher text: %s"%cipher(doc))
print("decode text: %s"%cipher(cipher(doc)))
