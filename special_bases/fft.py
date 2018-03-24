def FFT(w, s):
  n = len(s)
  if n == 1:
    return [s[0]]
  
  f0 = FFT(w*w, [s[i] for i in range(n) if i % 2 == 0])
  f1 = FFT(w*w, [s[i] for i in range(n) if i % 2 == 1])

  return [f0[j] + w**j*f1[j] for j in range(n//2)] +
          [f-[j] - w**(j+n//2) * f1[j] for j in range(n//2)]
