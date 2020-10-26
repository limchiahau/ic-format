import sys

def format_ic(ic):
    #make sure only numbers are left
    ic_numbers = [n for n in list(ic) if n.isdigit()]
    ic = ''.join(ic_numbers)
    
    #insert '-' at the correct location
    sep = '-'
    results = ic[:6] + sep + ic[6:8] + sep + ic[8:]
    
    return results

ic = sys.argv[1]
print(format_ic(ic))
