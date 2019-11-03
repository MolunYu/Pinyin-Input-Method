import sys
import time


def bar(obj, width=50):
    if hasattr(obj, "__len__"):
        total = len(obj)
        for i, j in enumerate(obj):
            yield j

            present = i / total
            use_num = int(present * width)
            space_num = int(width - use_num)

            sys.stdout.write("\r[{}{}]{:.1f}%".format(use_num * "#", space_num * " ", present * 100))
            sys.stdout.flush()
    else:
        for i, j in enumerate(obj):
            yield j

            if i % 100 == 0:
                sys.stdout.write("\r{}".format(10 * " "))
                sys.stdout.write("\r{}".format(((i // 100) % 5 + 1) * "."))
                sys.stdout.flush()

    sys.stdout.write("\r[{}]100%\n".format(50 * "#"))
    sys.stdout.flush()

