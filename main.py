from typing import List

def trap(height: List[int]) -> int:
    pass

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().strip().split("\n")
    height = list(map(int, input[1].split()))
    result = trap(height)
    print(result)
