"""
created by Nagaj at 05/06/2021
"""
from typing import Tuple


def is_valid_rgb(
    color: Tuple[int, ...]
) -> bool:  # at least one int item in tuple ==> Tuple[int, ...]
    if len(color) != 3:
        raise ValueError(
            "color must be in 3 values between 0 t0 255 (red, green, blue)"
        )
    for value in color:
        if value not in range(0, 256):
            return False
    return True


def is_valid_rgb_2(color: Tuple[int, ...]) -> bool:
    assert len(color) == 3, f"Invalid RGB color values {color}, Must Be (R, G, B)"
    # return all(value in range(0, 256) for value in color)
    return all(0 <= value <= 255 for value in color)


def main():
    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    random_color = (255, 255, 0, 9, 10)

    assert is_valid_rgb(red) is True
    assert is_valid_rgb(blue) is True
    assert is_valid_rgb(yellow) is True
    # assert is_valid_rgb(random_color) is True

    # ############### # ################ ################ ################ ###############
    print("#" * 100)
    assert is_valid_rgb_2((233, 55, 66)) is True
    assert is_valid_rgb_2((233, 255, 255)) is True
    assert is_valid_rgb_2((233, 255)) is True
    assert is_valid_rgb_2((233, 255, 30, 20)) is True
    print("ALL TESTS WERE PASSED")


if __name__ == "__main__":
    main()
