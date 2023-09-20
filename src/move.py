class Move:
    
    def __init__(self, initial_square, target_square):
        self.initial_square = initial_square
        self.target_square = target_square
        
    def __eq__(self, other):
        return self.target_square == other.target_square \
            and self.target_square == other.target_square
            
    def __iter__(self):
        return iter(
            [
                self.initial_square,
                self.target_square
            ]
        )