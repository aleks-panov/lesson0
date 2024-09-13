def all_variants(text):
   for i in range(len(text)):
        for k in range(len(text)-i):
            yield text[k:i+k+1]

a = all_variants("abc")
for i in a:
    print(i)