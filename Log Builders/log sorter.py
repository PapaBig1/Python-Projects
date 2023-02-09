import time

def main():
    file2search = input('Enter text file name: ')
    file2 = open (f'{file2search}.txt','r')
    file = file2.read()
    file2.close()

    sort = input('Press enter to sort: ')
    time.sleep(1)
    print('Sorting...')
    print()

    #Letters

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    w = 0
    x = 0
    y = 0
    z = 0



    #Count

    for count in file:
        if 'a' in count:
            a += 1
        elif 'b' in count:
            b += 1
        elif 'c' in count:
            c += 1
        elif 'd' in count:
            d += 1
        elif 'e' in count:
            e += 1
        elif 'f' in count:
            f += 1
        elif 'g' in count:
            g += 1
        elif 'h' in count:
            h += 1
        elif 'i' in count:
            i += 1
        elif 'j' in count:
            j += 1
        elif 'k' in count:
            k += 1
        elif 'l' in count:
            l += 1
        elif 'm' in count:
            m += 1
        elif 'n' in count:
            n += 1
        elif 'o' in count:
            o += 1
        elif 'p' in count:
            p += 1
        elif 'q' in count:
            q += 1
        elif 'r' in count:
            r += 1
        elif 's' in count:
            s += 1
        elif 't' in count:
            t += 1
        elif 'u' in count:
            u += 1
        elif 'v' in count:
            v += 1
        elif 'w' in count:
            w += 1
        elif 'x' in count:
            x += 1
        elif 'y' in count:
            y += 1
        elif 'z' in count:
            z += 1

    everything = a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z
    
    #File creation

    fileS = open (f'{file2search}_Sorted.txt','w')


    #File Sort

    for aS in range(a):
        fileS.write('a')
    for bS in range(b):
        fileS.write('b')
    for cS in range(c):
        fileS.write('c')
    for dS in range(d):
        fileS.write('d')
    for eS in range(e):
        fileS.write('e')
    for fS in range(f):
        fileS.write('f')
    for gS in range(g):
        fileS.write('g')
    for hS in range(h):
        fileS.write('h')
    for iS in range(i):
        fileS.write('i')
    for jS in range(j):
        fileS.write('j')
    for kS in range(k):
        fileS.write('k')
    for lS in range(l):
        fileS.write('l')
    for mS in range(m):
        fileS.write('m')
    for nS in range(n):
        fileS.write('n')
    for oS in range(o):
        fileS.write('o')
    for pS in range(p):
        fileS.write('p')

    for qS in range(q):
        fileS.write('q')
    for rS in range(r):
        fileS.write('r')
    for sS in range(s):
        fileS.write('s')
    for tS in range(t):
        fileS.write('t')
    for uS in range(u):
        fileS.write('u')
    for vS in range(v):
        fileS.write('v')
    for wS in range(w):
        fileS.write('w')
    for xS in range(x):
        fileS.write('x')
    for yS in range(y):
        fileS.write('y')
    for zS in range(z):
        fileS.write('z')

    #Say
    fileS.write('\n')
    fileS.write('\n')
    fileS.write(f'a was printed {a} times')
    fileS.write('\n')
    fileS.write(f'b was printed {b} times')
    fileS.write('\n')
    fileS.write(f'c was printed {c} times')
    fileS.write('\n')
    fileS.write(f'd was printed {d} times')
    fileS.write('\n')
    fileS.write(f'e was printed {e} times')
    fileS.write('\n')
    fileS.write(f'f was printed {f} times')
    fileS.write('\n')
    fileS.write(f'g was printed {g} times')
    fileS.write('\n')
    fileS.write(f'h was printed {h} times')
    fileS.write('\n')
    fileS.write(f'i was printed {i} times')
    fileS.write('\n')
    fileS.write(f'j was printed {j} times')
    fileS.write('\n')
    fileS.write(f'k was printed {k} times')
    fileS.write('\n')
    fileS.write(f'l was printed {l} times')
    fileS.write('\n')
    fileS.write(f'm was printed {m} times')
    fileS.write('\n')
    fileS.write(f'n was printed {n} times')
    fileS.write('\n')

    fileS.write(f'o was printed {o} times')
    fileS.write('\n')
    fileS.write(f'p was printed {p} times')
    fileS.write('\n')
    fileS.write(f'q was printed {q} times')
    fileS.write('\n')
    fileS.write(f'r was printed {r} times')
    fileS.write('\n')
    fileS.write(f's was printed {s} times')
    fileS.write('\n')
    fileS.write(f't was printed {t} times')
    fileS.write('\n')
    fileS.write(f'u was printed {u} times')
    fileS.write('\n')
    fileS.write(f'v was printed {v} times')
    fileS.write('\n')
    fileS.write(f'w was printed {w} times')
    fileS.write('\n')
    fileS.write(f'x was printed {x} times')
    fileS.write('\n')
    fileS.write(f'y was printed {y} times')
    fileS.write('\n')
    fileS.write(f'z was printed {z} times')
    fileS.write('\n')
    fileS.write(f'total: {everything} letters')
    fileS.write('\n')


if __name__ == '__main__':
    main()
