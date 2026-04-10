package utilities

import "iter"

func Permutations[T any](arr []T) iter.Seq[[]T] {
    return func(yield func([]T) bool) {
        nums := make([]T, len(arr))
        copy(nums, arr)

        var backtrack func(int) bool
        backtrack = func(start int) bool {
            if start == len(nums) {
                temp := make([]T, len(nums))
                copy(temp, nums)
                return yield(temp) // pause here; resume when caller is ready
            }
            for i := start; i < len(nums); i++ {
                nums[start], nums[i] = nums[i], nums[start]
                if !backtrack(start + 1) {
                    return false // caller broke out of range loop
                }
                nums[start], nums[i] = nums[i], nums[start]
            }
            return true
        }
        backtrack(0)
    }
}
