class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:  # 중복제거
                continue

            while left < right:
                sums = nums[i] + nums[left] + nums[right]
                if sums > 0:
                    right -= 1
                elif sums < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # 중복제거
                        left += 1
                    # while left<right and nums[right] == nums[right-1]:  # 중복제거 <- 이 조건 없어도 됨.
                    # right-=1

                    left += 1
                    # right-=1
        return res
