import time


def main():
    l_minimal = int(input())
    r_maximum = int(input())
    if l_minimal <= r_maximum:
        all_roots = []
        start_time = time.time()
        for i in range(l_minimal, r_maximum + 1):
            max_interal = 100000
            min_interval = -100000 + i
            interval = [max_interal, min_interval]
            while interval[1] != max_interal:
                now_disc = discriminant(interval[0], interval[1])
                if now_disc is not None:
                    all_roots.append(now_disc)
                interval[0] -= 1
                interval[1] += 1
        print(all_roots, "\n", len(all_roots))
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("l_minimal > r_maximum")


def discriminant(b_coef, c_coef):
    disc = b_coef ** 2 - 4 * c_coef
    if disc >= 0:
        root_of_disc = disc ** 0.5
        x1 = (-b_coef + root_of_disc) / 2
        x2 = (-b_coef - root_of_disc) / 2
        if x1 % 1 == 0 and x1 == x2 or x2 % 1 == 0:
            return x1, x2
    return None


if __name__ == "__main__":
    main()
