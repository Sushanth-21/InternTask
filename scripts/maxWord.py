f = open("maxWord.txt", "r")
s = f.read()
s = s.replace(",", " ")
# removing . and , from string and replacing it with white space. -,!,etc can be replaced as well using regex.
s = s.replace(".", " ")
# removing consecutive white spaces obtained as a result of replacing , and . with white space.
s = s.replace("  ", " ")
s = s.strip()  # removing white spaces at beginning and end of string, Obtained because of replacing a . with white space which is at the end of string
s = s.replace("\n", "")
l = s.split(" ")
d = {}
word = []
for i in l:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
max = max(d, key=d.get)
for key, value in d.items():
    if value == d[max]:
        word.append(key)
print(d)
print('COUNT - ', d[max], '\nWORDS - ')
for i in word:
    print(i)
f.close()
