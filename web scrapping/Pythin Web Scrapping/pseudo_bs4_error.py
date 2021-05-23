try:
    badContent = bsobj.notExistentTag.anotherTag
except AttributeError as e:
    print("Tag was not found")
else:
    print(badContent)
