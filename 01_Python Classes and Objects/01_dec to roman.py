
# Convert an integer it to a roman numeral

class int_to_roman:
    def roman(self,n):
        
        val=[1000, 900, 500, 400, 
              100, 90, 50, 40,
               10, 9, 5, 4,
                1]
    
        rom=["M", "CM", "D", "CD",
              "C", "XC", "L", "XL",
              "X", "IX", "V", "IV",
              "I"]
    
        roman_no=""
        i=0
        while True:
            if n//val[i]>=1:
                roman_no=roman_no+rom[i]
                n=n-val[i]
            else:    
                i+=1    
            if n==0:
                break
        return roman_no    

r = int_to_roman()
print(r.roman(184))