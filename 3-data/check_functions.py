<<<<<<< HEAD
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
=======
def clean_currency(value:str) -> float:
    '''
    This function will take a string value and remove the dollar sign and commas
    and return a float value.
    '''
    return float(value.replace(',', '').replace('$', ''))

def detect_whale(
        items_per_person:float, 
        price_per_person:float, 
        items_per_person_75th_pctile:float, 
        price_per_person_75_pctile:float) -> str:
    if items_per_person > items_per_person_75th_pctile and price_per_person > price_per_person_75_pctile:
        return 'whale'
    if items_per_person > items_per_person_75th_pctile:
        return 'big eater'
    if price_per_person > price_per_person_75_pctile:
        return 'big spender'
    
    return 'normal'


if __name__ == '__main__':
    assert clean_currency('$1,234.56') == 1234.56

    print("All tests passed!!")
           
>>>>>>> 3675e1bf6f97413e21695e2aadc0947aa4c9d2bb
