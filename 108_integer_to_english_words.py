# Time complexity - O(12) i.e. O(1) # Worst case is the number is in Billion, so 4 triplets to deal with
# Space complexity - O(3) i.e. O(1)

# Approach - Run a recursive function on the triplets, check if num is below 20, below 100, or rest. For
# all the triplets, maintain a variable to get suffix. Finally return result. 

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        self.suffix = ["", "Thousand", "Million", "Billion"]
        self.below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        i = 0
        result = ""
        while num > 0:
            if num%1000 != 0:
                result = self.helper(num%1000) + self.suffix[i] + " " + result
            num = num//1000
            i += 1
        return result.strip()

    
    def helper(self, num: int) -> None:
        if num == 0:
            return ""
        if num < 20:
            return self.below_20[num] + " "
        elif num < 100:
            return self.tens[int(num/10)] + " " + self.helper(num%10)
        else:
            return self.below_20[int(num/100)] + " Hundred " + self.helper(num%100)