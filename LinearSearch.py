    def linear_search(n: int, v: list[int]) -> int:
        """
        Searches vector to find the inputted integer using the Linear Search Algorithm. If found, returns 1. Else returns 0.
        Time Complexity: Theta(n)
        Space Complexity: Theta(1)

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
