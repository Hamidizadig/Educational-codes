words=('abccba','aabaa','lllllla','wwwwwowwwww','uuuuuuuuuuuu')
print(list(filter(lambda word: word==word[::-1],words)))