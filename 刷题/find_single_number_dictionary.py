def solution(cards):
    # Edit your code here
    list = {}
    for card in cards:
        if list.get(card):
            del list[card]
        else:
            list[card] = 1
    last_key = next(iter(list))
    return last_key

if __name__ == "__main__":
    # Add your test cases here

    print(solution([1, 1, 2, 2, 3, 3, 4, 5, 5]) == 4)
    print(solution([0, 1, 0, 1, 2]) == 2)
