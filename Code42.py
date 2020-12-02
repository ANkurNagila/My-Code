def highlight_word(sentence, word):
  t=sentence.split()
  f=[]
  for x in t:
    if word in x:
      x=x.upper()
    f.append(x)
  sentence=" ".join(f)
  return(sentence)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
