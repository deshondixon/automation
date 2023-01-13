import re


def validate(number):
    """
    Uses Regex to validate a phone number.
    :param number: string of integers
    :return: boolean
    """
    # thank you https://www.abstractapi.com/guides/phone-number-python-regex
    pattern = r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"  # regex
    # pattern

    # could be none or could be match group
    match_obj = re.match(pattern, number)

    if match_obj:
        return match_obj.group()
    else:
        return False


# list of good phone numbers
goodies = ["111-345-4563"]

# list of bad phone numbers
baddies = ["666-222-3222", "000-423-2342", "900-234-3424"]


if __name__ == "__main__":
    for number in goodies:
        assert validate(number)

#    for number in baddies:
#        assert not validate(number)

    print("TESTS PASS")
