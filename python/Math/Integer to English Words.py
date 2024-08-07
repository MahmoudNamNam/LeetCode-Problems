class Solution(object):
    def numberToWords(self, num):
        # Lists to store English words for numbers less than twenty and for multiples of ten
        less_than_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                            "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", 
                            "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        # Special case for zero
        if num == 0:
            return "Zero"

        # Helper function to convert numbers less than 1000 into words
        def to_words(n):
            if n < 20:
                # Directly use the less_than_twenty list for numbers less than 20
                return less_than_twenty[n]
            elif n < 100:
                # Combine tens place word with unit place word if necessary
                return tens[n // 10] + ('' if n % 10 == 0 else ' ' + less_than_twenty[n % 10])
            else:
                # Combine hundreds place word with the word "Hundred" and the remainder recursively
                return less_than_twenty[n // 100] + ' Hundred' + ('' if n % 100 == 0 else ' ' + to_words(n % 100))

        # Split the number into billions, millions, thousands, and the remainder
        billions, num = divmod(num, 1000000000)
        millions, num = divmod(num, 1000000)
        thousands, num = divmod(num, 1000)

        # List to store the words for each segment
        result = []
        if billions:
            # Convert billions segment to words if it's non-zero
            result.append(to_words(billions) + ' Billion')
        if millions:
            # Convert millions segment to words if it's non-zero
            result.append(to_words(millions) + ' Million')
            
        if thousands:
            # Convert thousands segment to words if it's non-zero
            result.append(to_words(thousands) + ' Thousand')
        if num:
            # Convert the remainder to words if it's non-zero
            result.append(to_words(num))
        
        # Join all parts with spaces and return the final result
        return ' '.join(result)



sol =Solution()

num = 1234567

print(sol.numberToWords(num))
