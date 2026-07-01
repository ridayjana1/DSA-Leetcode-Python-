from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0 
        basket = {}
        max_len = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            print(f"Fruits: {fruit}")
            basket[fruit] = basket.get(fruit, 0) + 1 #Expand right 
            print(f"Basket: {basket[fruit]}")

            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1
            curr_len = right - left + 1
            max_len = max(max_len, curr_len)

        return max_len



def main():

    test_cases = [

        ([1,2,1], 3),

        ([0,1,2,2], 3),

        ([1,2,3,2,2], 4),

        ([3,3,3,1,2,1,1,2,3,3,4], 5),

        ([1], 1),

        ([1,1,1,1], 4),

    ]

    sol = Solution()

    for fruits, expected in test_cases:

        result = sol.totalFruit(fruits)

        print("-" * 40)

        print(f"fruits          : {fruits}")

        print(f"Expected Output : {expected}")

        print(f"Your Output     : {result}")

        print("PASS" if result == expected else "FAIL")

if __name__ == "__main__":

    main()