
import numpy as np

is_red = lambda x: x % 2 == 0 and x != 0 
is_black = lambda x: x % 2 == 1
is_zero = lambda x: x == 0

# несовместные события
is_red_and_black = lambda x: is_red(x) and is_black(x)

# достоверное событие
is_red_or_black_or_zero = lambda x: is_red(x) or is_black(x) or is_zero(x)

TEST_COUNT = 1000

test = np.random.randint(0, 36, TEST_COUNT)

print(TEST_COUNT == len(list(filter(is_red_or_black_or_zero, test))))

print(0 == len(list(filter(is_red_and_black, test))))