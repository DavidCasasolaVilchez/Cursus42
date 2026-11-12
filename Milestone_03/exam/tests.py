# Level 2
def r2e2() -> None:
    nums: list[int] = [1, 2, 3, 4]
    inums: list[int] = nums[::-1]
    print(
        f"nums -> {nums}\ninverted nums -> {inums}"
    )


# Level 3
def hidenp(small: str, big: str) -> bool:
    start_index: int = 0
    chars_found: int = 0
    for c in small:
        for i in range(start_index, len(big)):
            if c == big[i]:
                chars_found += 1
                start_index = i + 1
                break
    return chars_found == len(small)


def r3e1() -> None:
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("ace", "abcde"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing", "subsequence testing"))


def inter(s1: str, s2: str) -> str:
    new_str: str = ""
    for c in s1:
        if s2.find(c) != -1 and new_str.find(c) == -1:
            new_str += c
    return new_str


def r3e2() -> None:
    print(f"\"{inter('hello', 'world')}\"")  # Expected: "lo"
    print(f"\"{inter('banana', 'band')}\"")  # Expected: "ban"
    print(f"\"{inter('abcabc', 'bc')}\"")  # Expected: "bc"
    print(f"\"{inter('abc', 'xyz')}\"")  # Expected: " "
    print(f"\"{inter('', 'abc')}\"")  # Expected: " "


# def number_base_converter(number: str, from_base: int, to_base: int) -> str:
#     base: str = "0123456789abcdefghijklmnopqrstuvwxyz"
#     base10: int = 0
#     for c in number:


# def r3e3() -> None:
#     print(number_base_converter("1010", 2, 10))  # Expected: "10"
#     print(number_base_converter("FF", 16, 10))  # Expected: "255"
#     print(number_base_converter("255", 10, 16))  # Expected: "FF"
#     print(number_base_converter("123", 10, 2))  # Expected: "1111011"
#     print(number_base_converter("Z", 36, 10))  # Expected: "35"
#     print(number_base_converter("35", 10, 36))  # Expected: "Z"
#     print(number_base_converter("123", 1, 10))  # Expected: "ERROR"
#     print(number_base_converter("G", 16, 10))  # Expected: "ERROR"


def string_sculptor(text: str) -> str:
    alph: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new: str = ""
    min: bool = True
    for c in text:
        if alph.find(c) != -1:
            if min:
                new += c.lower()
                min = False
            elif not min:
                new += c.upper()
                min = True
        else:
            new += c
    return new


def r5e1() -> None:
    print(string_sculptor("hello"))  # Expected: "hElLo"
    print(string_sculptor("Hello World"))  # Expected: "hElLo WoRlD"
    print(string_sculptor("   hello   "))  # Expected: "   hElLo   "
    print(string_sculptor("abc123def"))  # Expected: "aBc123DeF"
    print(string_sculptor("Python3.9!"))  # Expected: "pYtHoN3.9!"
    print(string_sculptor(""))  # Expected: ""


def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr:
        return arr

    k %= len(arr)
    return arr[-k:] + arr[:-k]


def r5e2() -> None:
    print(twist_sequence([1, 2, 3, 4, 5], 2))  # Expected: [4,5,1,2,3]
    print(twist_sequence([1, 2, 3], 1))  # Expected: [3,1,2]
    print(twist_sequence([1, 2, 3, 4], 0))  # Expected: [1,2,3,4]
    print(twist_sequence([1, 2, 3], 5))  # Expected: [2,3,1]
    print(twist_sequence([], 3))  # Expected: []


def main() -> None:
    r5e2()


if __name__ == "__main__":
    main()
