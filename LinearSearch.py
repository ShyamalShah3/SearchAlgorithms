    def linear_search(self, n: int, v: list[int]) -> int:
        """
        Searches vector to find the inputted integer. If found, returns 1. Else returns 0.

        Parameters
        ----------
        n : int
            The integer to search for in vector
        v : list[int]
            The vector to search in.
        """
        
        for x in v:
            if x == n: return 1
        return 0
