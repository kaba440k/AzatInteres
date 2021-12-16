import time


def main():
    l_minimal = int(input())
    r_maximum = int(input())
    start_time = time.time()
    all_roots = []
    if l_minimal <= r_maximum:
        for i in range(l_minimal, r_maximum + 1):
            if i == -1:
                all_roots.clear()
                print(-1)
                break
            else:
                interval = [100000, -100000 + i]
                while interval[1] != 100000:
                    if discriminant(interval[0], interval[1]) is not None:
                        all_roots.append(discriminant(interval[0], interval[1]))
                    interval[0] -= 1
                    interval[1] += 1
        if len(all_roots) != 0:
            print(all_roots, "\n", len(all_roots))
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("l_minimal > r_maximum")


def discriminant(b_coef, c_coef):
    disc = b_coef ** 2 - 4 * c_coef
    roots = [0, 0]
    if disc > 0:
        roots[0] = (b_coef * -1 + disc ** 0.5) / 2
        roots[1] = (b_coef * -1 - disc ** 0.5) / 2
        if roots[0] % 1 == 0 and roots[1] % 1 == 0:
            return roots
        else:
            return None
    else:
        return None


if __name__ == "__main__":
    main()
