from collections import Counter
import difflib

def solve_task_1():
    """
    TASK 1:
    To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID
    containing exactly two of any letter and then separately counting those with exactly three of any letter.
    You can multiply those two counts together to get a rudimentary checksum and compare it to what your device
    predicts.

    For example, if you see the following box IDs:

    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.
    Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter
    which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

    What is the checksum for your list of box IDs?
    """
    box_ids = list()
    with open("input.txt") as f:
        box_ids.extend([x.strip() for x in f.readlines()])

    two_ = 0
    three_ = 0
    for box_id in box_ids:
        counts = Counter(box_id)
        if 3 in counts.values():
            three_ += 1
        if 2 in counts.values():
            two_ += 1

    print(three_ * two_)


def solve_task_2():
    """
    TASK 2
    The boxes will have IDs which differ by exactly one character at the same position in both strings. For example,
    given the following box IDs:

    abcde
    fghij
    klmno
    pqrst
    fguij
    axcye
    wvxyz
    The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs
    fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

    What letters are common between the two correct box IDs? (In the example above, this is found by removing the
    differing character from either ID, producing fgij.)
    """

    with open("input.txt") as f:
        box_ids = list(map(lambda x: x.strip(), f.readlines()))

    for i in range(len(box_ids)):
        for j in range(i):
            different_char_indices = [w for w, x in enumerate(box_ids[i]) if box_ids[i][w] != box_ids[j][w]]
            if len(different_char_indices) == 1:
                res_box = box_ids[i][:different_char_indices[0]]+box_ids[i][different_char_indices[0]+1:]
                print(res_box)
                break


if __name__ == '__main__':
    solve_task_2()
