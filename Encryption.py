import random
import base64
#basic math stuff

keySize = 24;
alphanum = False;

basePrimes=[3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
			101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,
			181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,
			271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,
			373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,
			463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,
			577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,
			673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,
			787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,
			887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009,
			1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 
			1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 
			1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 
			1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 
			1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 
			1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 
			1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 
			1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 
			1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 
			1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 
			1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 
			1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 
			1997, 1999]

def rabinMillerPrimallity(n, k):
	s = n-1
	t = 0
	while s&1 == 0:
		s = s/2
		t +=1
	kLoop = 0
	while kLoop<k:
		a = random.randrange(2,n-1)
		v = pow(a,s,n)
		if v != 1:
			i=0
			while v != (n-1):
				if i == t-1:
					return False
				else:
					i = i+1
					v = (v**2)%n
		kLoop+=2
	return True
		
def isPrime(n, k): #checks if int n of length k is a prime
	if (n >= 3):
		if (n&1 != 0):
			for p in basePrimes:
				if (n == p):
					return True
				if (n % p == 0):
					return False
			return rabinMillerPrimallity(n, k)
	return False

def primeFactor(n):
	primfac = []
	d = 2
	while d*d <= n:
		while (n % d) == 0:
			primfac.append(d)
			n //= d
		d += 1
	if n > 1:
		 primfac.append(n)
	return primfac
			 
def randPrime(bitsize): # generates random prime between small and large
	r = random.randrange(2**(bitsize-1),2**(bitsize))
	while not isPrime(r, bitsize): 
		r = random.randrange(2**(bitsize-1),2**(bitsize))
	return r
	
def totient(p,q):
	return (p-1)*(q-1)
def coprime(a,b):
	aFactors = primeFactor(a)
	bFactors = primeFactor(b)
	for x in aFactors:
		for y in bFactors:
			if (x == y):
				return False
	return True
		
		
	
	
#generate public and private keys

# create two prime numbers
p = randPrime(keySize)
q = randPrime(keySize)
print p
print q


# find product of p and q
n = p*q
print "n"
# find totient 
nTot = totient(p,q)
print "ntot"
#generate e
# 1<e<nTot and e and n are coprime 
def generateE(nTot):
	e = random.randint(1,nTot)
	while not coprime(e,n):
		e = random.randint(1,nTot)
	return e

#e = generateE(nTot)
e = 65537;
print "e gen"
#find d (d*e)%nTot = 1
#def generateD(e,nTot):
#	d = 1;
#	while not ()
def generateDV1(e,nTot):
	y = 0;
	d = ((nTot*y)+1)/e
	while not ((d*e)%nTot == 1):
		d = ((nTot*y)+1)/e
		print e, d, (d*e)%nTot
		if (d > nTot*d):
			break
			e = generateE(nTot)
			d = generateD(e,nTot)
		y+=1
	return d
	
def generateDV2(e,nTot):
	while True:
		for d in range (1,nTot):
			if (d*e)%nTot ==1:
				return d
		e = generateE(nTot);
		print e
		print extendedEuclidian(e, nTot)
	
def generateDV3(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return x

d = generateDV3(e,nTot)





print 'p: ',p
print 'q: ',q
print 'n: ',n
print 'totient(n): ',nTot
print 'e: ',e
print 'd: ',d
if alphanum:
	n = base64.b64encode(bytes([n]))
	e = base64.b64encode(bytes([e]))
	d = base64.b64encode(bytes([d]));

print 'public exponent: ',(n)
print 'public modulus: ',(e)
print 'private exponent: ',(d)
#encryption
m = raw_input('message to encrypt(no spaces): ')
h = []
for letter in m:
	b = ord(letter)
	h.append(b)
print 'letter in ascii'
print h

c = []
for letter in h:
	b = int((letter**e)%n)
	c.append(b)
	
print 'encrypted letter: '
print c

message = []
for x in c:
	b = (x**d)%n
	message.append(str(unichr(b)))
print 'decrypted letter:'
print message


	
	
	
	
	