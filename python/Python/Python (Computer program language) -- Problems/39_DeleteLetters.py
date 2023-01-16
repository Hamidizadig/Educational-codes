def strip_chars(str,chars):
    return ''.join(c for c in str if c not in chars)
s=input('Original String : ')
strip1=input(' stripping chars: ')
print(strip_chars(s,strip1))