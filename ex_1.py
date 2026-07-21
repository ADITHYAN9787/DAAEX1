import time
import random


def interpolation_search(arr, target):
    """
    Interpolation Search Algorithm

    Time Complexity:
        Best Case    : O(1)
        Average Case : O(log log n)
        Worst Case   : O(n)

    Space Complexity:
        O(1)
    """

    low, high = 0, len(arr) - 1
    comparisons = 0

    while (
        low <= high
        and arr[low] <= target <= arr[high]
        and arr[high] != arr[low]
    ):
        comparisons += 1

        # Interpolation Formula
        pos = low + int(
            ((target - arr[low]) * (high - low))
            / (arr[high] - arr[low])
        )

        if arr[pos] == target:
            return pos, comparisons

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    # Handle the case when low == high
    if low <= high and low < len(arr) and arr[low] == target:
        comparisons += 1
        return low, comparisons

    return -1, comparisons


def binary_search(arr, target):
    """
    Binary Search Algorithm

    Time Complexity:
        Best Case    : O(1)
        Average Case : O(log n)
        Worst Case   : O(log n)

    Space Complexity:
        O(1)
    """

    low, high = 0, len(arr) - 1
    comparisons = 0

    while low <= high:
        comparisons += 1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, comparisons

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1, comparisons


def performance_analysis():
    """Compare Interpolation Search with Binary Search."""

    sizes = [1000, 5000, 10000, 50000, 100000]

    print(
        f"{'Size':>10} {'IS Time(ms)':>14} {'BS Time(ms)':>14} "
        f"{'IS Comparisons':>18} {'BS Comparisons':>18}"
    )
    print("-" * 80)

    for size in sizes:
        arr = sorted(random.sample(range(size * 10), size))
        target = arr[random.randint(0, size - 1)]

        # Interpolation Search Timing
        start = time.perf_counter()
        for _ in range(100):
            idx_is, comp_is = interpolation_search(arr, target)
        is_time = (time.perf_counter() - start) / 100 * 1000

        # Binary Search Timing
        start = time.perf_counter()
        for _ in range(100):
            idx_bs, comp_bs = binary_search(arr, target)
        bs_time = (time.perf_counter() - start) / 100 * 1000

        print(
            f"{size:>10} "
            f"{is_time:>14.6f} "
            f"{bs_time:>14.6f} "
            f"{comp_is:>18} "
            f"{comp_bs:>18}"
        )


def main():
    # Sample Input
    arr = [2, 5, 10, 15, 23, 35, 48, 60, 75, 90, 105, 120]
    target = 35

    idx, comps = interpolation_search(arr, target)

    print("Interpolation Search Example")
    print("-" * 35)
    print("Array:", arr)
    print("Target:", target)

    if idx != -1:
        print(f"Element found at index: {idx}")
    else:
        print("Element not found.")

    print(f"Comparisons: {comps}\n")

    print("Performance Analysis")
    print("=" * 80)
    performance_analysis()


if __name__ == "__main__":
    main()
