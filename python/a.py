import sys

z = "jyot "
zz = z
zzz = zz

print("Value of z:", z)
print("ID of z:", id(z))
print("Reference count of z:", sys.getrefcount("jyot"))
