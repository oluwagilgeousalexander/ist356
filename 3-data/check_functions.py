'''module for 3-4-1.py'''

def clean_currency(value: str) -> float:
    """Convert a currency string to a float."""
    value = value.replace(',', '')
    value = value.replace('$', '')
    float_value = float(value)
    return float_value
   # return float(value.replace("$", "").replace(",", "")) -- one line version of the function, not used in order to make the function easier to read and debug

def items_per_person(total_items: int, party_size: int) -> float:
    """Calculate the number of items per person."""
    return total_items / party_size

def detect_whale(value: float) -> str:
    '''this functions detects a big spender, or "whale" based on a threshold of a 75th percentile of the total amount of checks in the dataset'''
    if items_per_person > 10:
        return "Whale"
    if items_per_person > 5:
        return "Big Spender"
    if items_per_person > 2:
        return "normie"

if __name__ == "__main__":
    # test clened_currency function
    test_value = "$1,234.56"
    assert clean_currency(test_value) == 1234.56, f"Expected 1234.56 but got {clean_currency(test_value)}"
    print("\nAll test passed!")