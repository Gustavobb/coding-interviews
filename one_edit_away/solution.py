# Given two strings, write a function that checks if they are one (or zero) edit away from each other.
# Edit: there are three types of edit operations - insert, remove, or replace a character;
# -> Uppercase and lowercase letters must be considered different;
# -> Strings may contain any valid character.

# Examples:
# pale, ple -> true
# pale, pales -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false

def one_replace_away(first: str, second: str) -> bool:
    """
    Given two strings checks if they are one (or zero) replace away from each other.
    """
    has_replaced = False
    for i in range(len(first)):
        if first[i] != second[i]:
            if has_replaced: return False
            has_replaced = True

    return True

def one_insert_delete_away(first: str, second: str, len_diff: int) -> bool:
    """
    Given two strings checks if they are one (or zero) insert/delete away from each other.
    """
    longest_string = second
    shortest_string = first
    if len_diff > 0:
        longest_string = first
        shortest_string = second

    j = 0
    has_replaced = False

    for i in range(len(longest_string)):
        j %= len(shortest_string)
        if longest_string[i] != shortest_string[j]:
            if has_replaced: return False
            has_replaced = True
            j -= 1
        
        j += 1
    
    return True

def one_edit_away(first: str, second: str) -> bool:
    """
    Given two strings checks if they are one (or zero) edit away from each other.
    """
    len_diff = len(first) - len(second)
    if len_diff >= 2: return False
    if len_diff == 0: return one_replace_away(first, second)
    return one_insert_delete_away(first, second, len_diff)

def main() -> int:
    """
    Main function
    """
    assert one_edit_away("pale", "ple") == True
    assert one_edit_away("pale", "pales") == True
    assert one_edit_away("pales", "pale") == True
    assert one_edit_away("pale", "bale") == True
    assert one_edit_away("pale", "bake") == False

if __name__ == "__main__":
    exit(main());