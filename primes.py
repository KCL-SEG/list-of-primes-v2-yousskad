"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def ftPrime(num):
    
  if(num==1 or num==0):
    return False

  for counter in range(2,num):

    if(num%counter==0):
      return False
    
  return True

def primes(number_of_primes):
    if(number_of_primes < 1):
        raise ValueError('Your Number is < 1 ')
    list = []
    num = 0
    while(len(list) < number_of_primes):
        if(ftPrime(num)):
            list.append(num)
                        
        num= num+1
    return list
