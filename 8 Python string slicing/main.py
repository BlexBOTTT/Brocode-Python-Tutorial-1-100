# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

# indexing[]
name = "Blex Kwarante"

first_name = name[:4]           # [0:4]
last_name = name[5:]            # [5:end]
funky_name = name[::2]          # [0:end:2]
reversed_name = name[::-1]      # [0:end:-1]

# Blex
print(first_name)
# Kwarante
print(last_name)
# Be wrne = 2  b x w a e = 3
print(funky_name)
# etnarawK xelB
print(reversed_name)

# slice
website_1 = "http://google.com"
website_2 = "http://instagram.com"

slicetest = slice(7, -4)

print()
print(website_1[slicetest])
print(website_2[slicetest])
