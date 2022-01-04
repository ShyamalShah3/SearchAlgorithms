    def binary_search_iterative(n: int, v: list[int]) -> int:
        """
        Searches vector to find the inputted integer using an iterative Binary Search Algorithm. 
        If found, returns 1. Else returns 0.
        Time Complexity: Theta(log(n))
        Space Complexity: Theta(1)

        Parameters
        ----------
        n : int
            The integer to search for in vector
        v : list[int]
            The vector to search in.
        """
        start = 0
        end = len(v)-1
        while start <= end:
            mid = (start+end) // 2  # floor division
            temp = v[mid]
            if temp == n:
                return 1
            elif n < temp:
                end = mid - 1
            else:
                start = mid + 1
        return 0
