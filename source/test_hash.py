
HASH_MAX = ((2 ** 32) - 1)

# Dummy hash function based on mersenne primes
# to be replaced with actual hash function

def minerHash(addr, pair, buyInd, sellInd, nonce):
    comp1 = addr * ((2 ** 31) - 1)
    comp2 = pair * ((2 ** 37) - 1)
    comp3 = buyInd * ((2 ** 41) - 1)
    comp4 = sellInd * ((2 ** 43) - 1)
    comp5 = nonce * ((2 ** 47) - 1)
    ret = (comp1 + comp2 + comp3 + comp4 + comp5) % HASH_MAX
    return ret

