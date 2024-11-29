def solution(s: str) -> str:
    s = s.lstrip('0')
    try:
        ineger_str, small = s.split('.')
    except:
        ineger_str, small = s, '0'
    sections = len(ineger_str)//3 + \
        (lambda: 1 if len(ineger_str) % 3 > 0 else 0)()
    index_list = [3*x-2 for x in range(1, sections+1)]
    splitted_reversed_inter = [
        ineger_str[(-1)*index-2: None if ((-1)*index+1) == 0 else (-1)*index+1] for index in index_list]
    splitted_reversed_inter.reverse()
    splitted_inter = splitted_reversed_inter
    splitted_inter = ','.join(splitted_inter)
    # right_str = None if float(small)%1==0 else ('.' + small)
    result_str = splitted_inter if float(
        small) == 0 else (splitted_inter + '.' + small)
    return result_str


if __name__ == '__main__':
    print(solution("1294512.12412") == '1,294,512.12412')
    print(solution("0000123456789.99") == '123,456,789.99')
    print(solution("987654321") == '987,654,321')
