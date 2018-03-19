def dict2list(dct, keylist):
  return [dct[key] for key in keylist]

def list2dict(L, keylist):
  return {keylist[i]: L[i] for i in range(len(keylist))}
