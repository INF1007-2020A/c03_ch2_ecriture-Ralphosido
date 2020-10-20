#!/usr/bin/env python
import math

def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.

    p = ((voltage) ^ 2) / resistance
    return p

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	m1 = math.sqrt((v1[0]) ** 2 + (v1[1]) ** 2)
	m2 = math.sqrt((v2[0]) ** 2 + (v2[1]) ** 2)
	v3 = v1 + v2
	m3 = math.sqrt((v3[0]) ** 2 + (v3[1]) ** 2)
	ps = m1 ** 2 + m2 ** 2 - m3 ** 2
	if ps == 0:
		print("vrai")
	else:
		print("faux")



def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	for x in values:
		if x < 0:
			values.remove(x)
	s = 0
	for x in values:
		s += x
		m = s / len(values)
	return m


def bills(value):
	twenties = int(value / 20)
	x = value % 20
	tens = int(x / 10)
	y = x % 10
	fives = int(y / 5)
	z = y % 5
	twos = int(z / 2)
	ones = z % 2



	return (twenties, tens, fives, twos, ones);

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1,1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
