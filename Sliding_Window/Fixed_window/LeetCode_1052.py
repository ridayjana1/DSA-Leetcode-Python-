from typing import List
from zipfile import MAX_EXTRACT_VERSION

# class Solution:
#     def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
#         bonus = []
        
#         base_satisfied = 0
        
        
#         for i in range(len(customers)):
#             if grumpy[i] == 0:
#                 base_satisfied += customers[i]
#                 print(base_satisfied)
#                 bonus.append(0)               
#             elif grumpy[i] == 1:
#                 bonus.append(customers[i])
#                 print(bonus)
#         total_bonus = sum(bonus[:minutes])
#         max_extra = total_bonus        
#             # print(total_bonus)
            
       
#         for i in range(minutes, len(bonus)):
#             total_bonus += bonus[i]
#             total_bonus -= bonus[i - minutes]
#             print(f"what is the total bonus: {total_bonus}")
#             max_extra = max(max_extra, total_bonus)
            
#         return base_satisfied + max_extra  MY SOLUTION 

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        base_satisfied = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                base_satisfied += customers[i]

        window_bonus = 0

        for i in range(minutes):
            if grumpy[i] == 1:
                window_bonus += customers[i]

        max_extra = window_bonus

        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                window_bonus += customers[i]

            if grumpy[i - minutes] == 1:
                window_bonus -= customers[i - minutes]

            max_extra = max(max_extra, window_bonus)

        return base_satisfied + max_extra #CHATGPT solution
         
            

                

            # if grumpy[i] == 1:
                
            #     window_info += customers[i]
            #     print(f"with the index {grumpy[i]}, what is window_info:{window_info}")
            
        # print(base_satisfied)
        




def main():
    customers = [4,10,10]
    grumpy =    [1,1,0]
    minutes = 2

    sol = Solution()
    result = sol.maxSatisfied(customers, grumpy, minutes)

    print("Answer: ", result)


if __name__ == "__main__":
    main()