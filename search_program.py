def binary_search(arr, target):
    """Perform binary search on sorted array."""
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low += 1
        else:
            high -= 1

    return -1

def main():
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = int(input("Enter target element: "))

    index = binary_search(arr, target)

    if index != -1:
        print(f"Element {target} found at index {index}.")
    else:
        print("Element not found.")

if __name__ == "__main__":
    main()
    