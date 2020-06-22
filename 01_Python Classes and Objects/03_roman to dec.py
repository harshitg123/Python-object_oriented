# this program is to decode roman values into
# decimal values

class dec:
    def rom_to_dec(self,n):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        su=0
        for i in range(len(n)):
            if i>0 and rom_val[n[i]] > rom_val[n[i-1]]:
                su=su+rom_val[n[i]]-2*rom_val[n[i-1]]
            else:
                su=su+rom_val[n[i]]
        return su 

dec=dec()
print(dec.rom_to_dec(input()))

# we have done this question by making the class dec