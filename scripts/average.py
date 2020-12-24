f = open("average.txt", "r")
s = f.read()
s = s.replace(",", " ")
# removing . and , from string and replacing it with white space. -,!,etc can be replaced as well using regex.
s = s.replace(".", " ")
# removing consecutive white spaces obtained as a result of replacing , and . with white space.
s = s.replace("  ", " ")
s = s.strip()  # removing white spaces at beginning and end of string, Obtained because of replacing a . with white space which is at the end of string
s = s.replace("\n", "")
l = s.split(" ")
l1 = []
for i in l:
    if i.endswith('ed') or i.endswith('ing'):
        l1.append(len(i))
print('AVERAGE - ', sum(l1)/len(l1))
