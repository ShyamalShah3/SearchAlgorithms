    def binary_search_recursive(n: int, v: list[int], low: int, high: int) -> int:
        """
        Searches vector to find the inputted integer using a recursive Binary Search Algorithm.
        If found, returns 1. Else returns 0.
        Time Complexity: Theta(log(n))
        Space Complexity: Theta(log(n))

        Parameters
        ----------
        n : int
            The integer to search for in vector
        v : list[int]
            The vector to search in. Assumed to be sorted in ascending order.
        low: int
            The index of the smallest element in the vector that could still contain n. Starts with a value of: 0.
        high: int
            The index of the largest element in the vector that could still contain n. Starts with a value of: |v| - 1.
        """
        if low <= high:
            mid = (low + high) // 2  # floor division
            temp = v[mid]

            if temp == n:
                return 1
            elif temp < n:
                return binary_search_recursive(n, v, low, mid - 1)
            else:
                return binary_search_recursive(n, v, mid + 1, high)
        return 0
