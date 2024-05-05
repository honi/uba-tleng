M1 = {
    (0, 'a'): 1,
    (0, 'b'): 0,
    (0, 'c'): 0,
    (1, 'a'): 2,
    (1, 'b'): 0,
    (1, 'c'): 2,
    (2, 'a'): 2,
    (2, 'b'): 2,
    (2, 'c'): 2,
}

M2 = {
    (0, 'a'): 0,
    (0, 'b'): 1,
    (0, 'c'): 0,
    (1, 'a'): 1,
    (1, 'b'): 0,
    (1, 'c'): 1,
}

M3 = {
    (0, 'a'): 0,
    (0, 'b'): 0,
    (0, 'c'): 1,
    (1, 'a'): 0,
    (1, 'b'): 0,
    (1, 'c'): 1,
}

def main():
    Q = [(0,0,0)]
    marked = [(0,0,0)]
    while Q:
        q, p, r = Q.pop(0)
        for c in "abc":
            q2 = M1[(q, c)]
            p2 = M2[(p, c)]
            r2 = M3[(r, c)]
            print(f"({q}{p}{r}, {c}) --> {q2}{p2}{r2}")

            n = (q2, p2, r2)
            if n not in marked:
                marked.append(n)
                Q.append(n)

if __name__ == "__main__":
    main()
