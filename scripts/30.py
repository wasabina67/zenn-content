def r(nums):
    if not nums:
        return []
    result = []
    start = nums[0]

    for i, num in enumerate(nums[1:], 1):
        if num - nums[i-1] != 1:
            result.append(
                str(start) if start == nums[i-1] else f"{start}~{nums[i-1]}"
            )
            start = num

    result.append(
        str(start) if start == nums[-1] else f"{start}~{nums[-1]}"
    )
    return result


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 8, 9, 10, 12, 13]
    print(r(numbers))  # ['1~5', '8~10', '12~13']
