import numpy as np


def solve_task_1():
    """
    TASK 1:
    Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and
    consist of a single rectangle with edges parallel to the edges of the fabric.
    Each claim's rectangle is defined as follows:

    The number of inches between the left edge of the fabric and the left edge of the rectangle.
    The number of inches between the top edge of the fabric and the top edge of the rectangle.
    The width of the rectangle in inches.
    The height of the rectangle in inches.
    A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches
    from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented
    by # (and ignores the square inches of fabric represented by .) in the diagram below:

    ...........
    ...........
    ...#####...
    ...#####...
    ...#####...
    ...#####...
    ...........
    ...........
    ...........
    The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas.
    For example, consider the following claims:

    #1 @ 1,3: 4x4
    #2 @ 3,1: 4x4
    #3 @ 5,5: 2x2
    Visually, these claim the following areas:

    ........
    ...2222.
    ...2222.
    .11XX22.
    .11XX22.
    .111133.
    .111133.
    ........
    The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others,
    does not overlap either of them.)

    If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of
    fabric are within two or more claims?
    """

    max_width = 0
    max_height = 0
    rectangles = list()
    with open("input.txt", "r") as f:
        for line in f:
            items = line.strip().split(" ")
            x0 = int(items[2].split(",")[0])
            y0 = int(items[2].split(",")[1][:-1])
            x1 = x0 + int(items[3].split("x")[0])
            y1 = y0 + int(items[3].split("x")[1])
            max_height = max(max_height, y1)
            max_width = max(max_width, x1)
            rectangles.append([x0, y0, x1, y1])

    # create empty piece of fabric
    fabric = np.zeros((max_width, max_height))

    # mark all pieces covered ba a claim
    for x0, y0, x1, y1 in rectangles:
        fabric[x0:x1, y0:y1] += 1

    marked = fabric[np.where(fabric >= 2.0)]
    print(len(marked))


def solve_task_2():
    """
    TASK 2
    Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch of fabric with
    any other claim. If you can somehow draw attention to it, maybe the Elves will be able to make Santa's suit after
    all!

    For example, in the claims above, only claim 3 is intact after all claims are made.

    What is the ID of the only claim that doesn't overlap?
    """

    max_width = 0
    max_height = 0
    rectangles = []
    with open("input.txt", "r") as f:
        for line in f:
            items = line.strip().split(" ")
            claim_id = items[0]
            x0 = int(items[2].split(",")[0])
            y0 = int(items[2].split(",")[1][:-1])
            x1 = x0 + int(items[3].split("x")[0])
            y1 = y0 + int(items[3].split("x")[1])
            max_height = max(max_height, y1)
            max_width = max(max_width, x1)
            rectangles.append((claim_id, [x0, y0, x1, y1]))

    # create empty piece of fabric
    fabric = np.zeros((max_width, max_height))

    # mark all pieces covered ba a claim
    for (claim_id, [x0, y0, x1, y1]) in rectangles:
        fabric[x0:x1, y0:y1] += 1

    for (claim_id, [x0, y0, x1, y1]) in rectangles:
        if np.all(fabric[x0:x1, y0:y1] == 1):
            print(claim_id)


if __name__ == '__main__':
    solve_task_2()
