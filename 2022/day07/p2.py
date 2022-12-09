#!/usr/bin/env python3

import collections
import fileinput
import pprint
import string
import typing


def main() -> None:
    dsizes = collections.defaultdict(int)
    dsizes["/"] += 0
    pwd: typing.List[str] = ["/", ]
    for line in fileinput.input():
        sline = line.strip()
        if sline.startswith("$ "):
            # command
            if " cd " in sline:
                # cd
                if " /" in sline:
                    pwd = ["/", ]
                elif ".." in sline:
                    pwd.pop()
                else:
                    pwd.append(sline.split(" ")[-1] + "/")
            else:
                # ls
                continue
        else:
            stat, name = sline.split(" ")
            if stat == "dir":
                continue
            size = int(stat)
            running = []
            for d in pwd:
                running.append(d)
                p = "".join(running)
                dsizes[p] += size

    total_size = 70000000
    required_free_space = 30000000
    current_free_space = total_size - dsizes["/"]
    space_to_free = required_free_space - current_free_space

    size_sum = 0
    smallest_delta = total_size
    for dname, dsize in dsizes.items():
        if dsize > 100000:
            pass
        else:
            size_sum += dsize
        if dsize > space_to_free and dsize < smallest_delta:
            smallest_delta = dsize

    print(f"size_sum p1 {size_sum}, smallest_dir_size p2 {smallest_delta}")


if __name__ == "__main__":
    main()
