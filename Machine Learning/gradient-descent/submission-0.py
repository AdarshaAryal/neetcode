class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
    
        minimiser = init

        for _ in range(iterations):
            derivative = 2 * minimiser
            minimiser = minimiser - learning_rate * derivative
        
        return round(minimiser, 5)