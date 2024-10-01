class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # Base case: if the expression is a number, return it as the only result
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        
        # Iterate over the expression to find operators
        for i, char in enumerate(expression):
            if char in '+-*':
                # Recursively compute the results of the left and right sub-expressions
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                
                # Combine the results from left and right sub-expressions
                for left in left_results:
                    for right in right_results:
                        if char == '+':
                            results.append(left + right)
                        elif char == '-':
                            results.append(left - right)
                        elif char == '*':
                            results.append(left * right)
        
        return results
