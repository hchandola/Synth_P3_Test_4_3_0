from typing import List

def sat190(x: float, str_nums=['1,3', '-11', '17.5', '-11', '2', '2.2', '2,2', '4', '-18,18', '99.09']):
    found = False
    for s in str_nums:
        y = float(s.replace(",", "."))
        assert y <= x
        if y == x:
            found = True
    return found
def sol190(str_nums=['1,3', '-11', '17.5', '-11', '2', '2.2', '2,2', '4', '-18,18', '99.09']):
    """Find the largest number where commas or periods are decimal points

    ["99,9", "100"] => 100.0
    """
    return max(float(s.replace(",", ".")) for s in str_nums)
# assert sat190(sol190())
