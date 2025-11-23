def calculate_avg(numbers: list[float]) -> float:
    """Calculate the average of a list of numbers.

    Returns 0.0 for an empty list.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def binary_search(arr: list[int], target: int) -> int:
    """Perform iterative binary search on sorted list `arr`.

    Returns the index of `target` if found, otherwise returns -1.

    Time complexity: O(log n)
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    # Simple demo: array MUST be sorted for binary search to work
    data = [1, 3, 5, 7, 9, 11]
    targets = [7, 2, 11]
    for t in targets:
        idx = binary_search(data, t)
        if idx != -1:
            print(f"Found {t} at index {idx}.")
        else:
            print(f"{t} not found in list (returned {idx}).")

            def quicksort(arr: list[int]) -> list[int]:
                """Return a new sorted list using quicksort (recursive, not in-place)."""
                if len(arr) <= 1:
                    return arr[:]
                pivot = arr[len(arr) // 2]
                less = [x for x in arr if x < pivot]
                equal = [x for x in arr if x == pivot]
                greater = [x for x in arr if x > pivot]
                return quicksort(less) + equal + quicksort(greater)


            if __name__ == "__main__":
                unsorted = [3, 6, 8, 10, 1, 2, 1]
                print("unsorted:", unsorted)
                print("quicksorted:", quicksort(unsorted))



def calculate_sum(numbers: list[float]) -> float:
    """Calculate the sum of a list of numbers without using the built-in sum."""
    total = 0.0
    for n in numbers:
        total += float(n)
    return total