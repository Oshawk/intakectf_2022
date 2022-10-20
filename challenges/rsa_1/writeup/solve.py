from math import isqrt, lcm

from Crypto.Util.number import isPrime


# https://rosettacode.org/wiki/Integer_roots#Python
def root(a, b):
    if b < 2:
        return b
    a1 = a - 1
    c = 1
    d = (a1 * c + b // (c ** a1)) // a
    e = (a1 * d + b // (d ** a1)) // a
    while c not in (d, e):
        c, d, e = d, e, (a1 * e + b // (e ** a1)) // a
    return min(d, e)


def main():
    e = 3
    n = 18248115999147265719349421179527162797840605606225773686639226953859804722611128825242080618926726843201681381270986490033713546540385935620777644008067956139564240175396786632962956407306722759881531973013236666663066968413291465989912464342508955934542193088197556069017512935579516565800490010094137287005005364485681933092283908475517565532954019833226027847120022026988980426591577686901443163546258962425063858076927230532351168390553994739080544956733941486812192582024673246545482063097059371973636592511833796921031720161160900462744206059004583431163590820221154150832198009755309046664501362808919434549263
    ct = 56274920108030879147510587900718628021081259042547196560477922498913815769467730659119705612390829987009186361032825981129859643199572873465457465957927246181

    pt = root(3, ct)

    print(pt.to_bytes(32, "big").lstrip(b"\x00"))


if __name__ == '__main__':
    main()
