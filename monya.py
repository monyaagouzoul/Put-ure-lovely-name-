Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> """
To run the Code u simply have to enter ure name
Hope u like it
Have a nice&blessed day 

Coded by: monya agouzoul
"""

alpha = {
  'A': ["aH","J","CdC","CdC","J","J","CdC","CdC"],
  'B': ["I","J","CdC","I","I","CdC","J","I"],
  'C': ["aH","J","CdC","Cg","Cg","CdC","J","aH"],
  'D': ["Gc","I","CdC","CdC","CdC","CdC","I","G"],
  'E': ["I","I","C","I","I","C","I","I"],
  'F': ["I","I","C","H","H","C","C","C"],
  'G': ["aH","J","C","CbE","CbE","CdC","J","aH"],
  'H': ["CdC","CdC","CdC","J","J","CdC","CdC","CdC"],
  'I': ["H","H","bD","bD","bD","bD","H","H"],
  'J': ["fD","fD","fD","fD","fD","CcD","J","aH"],
  'K': ["CcD","CbD","CaD","G","G","CaD","CbD","CcD"],
  'L': ["C","C","C","C","C","C","I","I"],
  'M': ["CfC","DdD","EbE","L","CaDaC","CbBbC","CfC","CfC"],
  'N': ["CdC","DcC","EbC","FaC","CaF","CbE","CcD","CdC"],
  'O': ["aH","J","CdC","CdC","CdC","CdC","J","aH"],
  'P': ["I","J","CdC","J","I","C","C","C"],
  'Q': ["aH","J","DcC","CaAbC","CbAaC","CcD","J","aH"],
  'R': ["I","J","CdC","J","I","CaD","CbD","CcD"],
  'S': ["aI","J","C","I","aI","gC","J","I"],
  'T': ["L","L","dD","dD","dD","dD","dD","dD"],
  'U': ["CfC","CfC","CfC","CfC","CfC","DdD","aJ","cF"],
  'V': ["CgC","CgC","CgC","aCeC","bCcC","cCaC","dE","eC"],
  'W': ["CfC","CfC","CbBbC","CaDaC","L","EbE","DdD","CfC"],
  'X': ["DeD","aDcD","bDaD","cG","cG","bDaD","aDcD","DeD"],
  'Y': ["DfD","aDdD","bDbD","cH","dF","eD","eD","eD"],
  'Z': ["I","I","dD","cD","bD","aD","I","I"]  
  }

txt=input()
def disp(text):
  for c in range(len(text)):
    flag=text[c].isupper()
    for i in range(64 if flag else 96, ord(text[c])):
      print('5' if flag else ' ', end='')
  print()

for i in range(len(txt)):
    if txt[i]==' ':
        print('\n\n')
        continue
    for r in range(8):
        disp('p'+alpha[txt[i].upper()][r])
    print('\n')
hello=("If u like it buy me an icecream *-*, else : \n maybe a coffee :p !")


print("{}\n\t hello :{}".format("$*$"*50,hello))
