### Python
```python
# version 1: TLE
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    max_sum = None
    for nidx in range(len(nums)):
      for kidx in range(nidx+1, len(nums)+1):
        s = sum(nums[nidx:kidx])
        if (max_sum is None):
          max_sum = s
          continue
        if (s > max_sum):
          max_sum = s
    return max_sum

# version 2: TLE
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    max_sum = None
    for nidx in range(len(nums)):
      s = None
      for k in nums[nidx:]:
        if (s is None):
          s = k
        else:
          s += k
        if (max_sum is None):
          max_sum = s
          continue
        if (s > max_sum):
          max_sum = s
    return max_sum

# version 3: WA
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    max_sum = None
    for nidx in range(len(nums)):
      # NOTE: there is not all subarray, eg. [2, 1, 2], same for the reversed
      # [3, 2, 1, 2, 3]
      # [2, 1, 2, 3]
      # [1, 2, 3]
      # [2, 3]
      # [3]
      s = sum(nums[nidx:])
      if (max_sum is None):
        max_sum = s
        continue
      if (s > max_sum):
        max_sum = s
    return max_sum
```

### C++
```cpp
# version 1: RE
class Solution {
  public:
    int maxSubArray() {
      // std::vector<int> nums = {-2,1,-3,4,-1,2,1,-5,4};
      int f = 0;
      int max_sum;
      for (int i=0; i < nums.size(); i++) {
        int next_vector_size = (nums.size() - i);
        int inner_sum = nums[i];
        for (int j=i; j < next_vector_size; j++) {
          inner_sum += nums[j+1];
        }
        if (f == 0) {
          f = 1;
          max_sum = inner_sum;
          continue;
        }
        if (max_sum < inner_sum) {
          max_sum = inner_sum;
        }
      }
      return max_sum;
    }
};

int main(void) {
  Solution s;
  printf("MAX_SUBARRAY: %d\n", s.maxSubArray());
}

/*
 * =================================================================
 * ==30==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6020000000f4 at pc 0x0000003455b9 bp 0x7ffd918b5450 sp 0x7ffd918b5448
 * READ of size 4 at 0x6020000000f4 thread T0
 *     #2 0x7fc65c8ae0b2  (/lib/x86_64-linux-gnu/libc.so.6+0x270b2)
 * 0x6020000000f4 is located 0 bytes to the right of 4-byte region [0x6020000000f0,0x6020000000f4)
 * allocated by thread T0 here:
 *     #6 0x7fc65c8ae0b2  (/lib/x86_64-linux-gnu/libc.so.6+0x270b2)
 * Shadow bytes around the buggy address:
 *   0x0c047fff7fc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
 *   0x0c047fff7fd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
 *   0x0c047fff7fe0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
 *   0x0c047fff7ff0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
 *   0x0c047fff8000: fa fa fd fa fa fa fd fa fa fa fd fa fa fa fd fa
 * =>0x0c047fff8010: fa fa fd fd fa fa fd fa fa fa fd fa fa fa[04]fa
 *   0x0c047fff8020: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
 *   0x0c047fff8030: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
 *   0x0c047fff8040: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
 *   0x0c047fff8050: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
 *   0x0c047fff8060: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
 * Shadow byte legend (one shadow byte represents 8 application bytes):
 *   Addressable:           00
 *   Partially addressable: 01 02 03 04 05 06 07
 *   Heap left redzone:       fa
 *   Freed heap region:       fd
 *   Stack left redzone:      f1
 *   Stack mid redzone:       f2
 *   Stack right redzone:     f3
 *   Stack after return:      f5
 *   Stack use after scope:   f8
 *   Global redzone:          f9
 *   Global init order:       f6
 *   Poisoned by user:        f7
 *   Container overflow:      fc
 *   Array cookie:            ac
 *   Intra object redzone:    bb
 *   ASan internal:           fe
 *   Left alloca redzone:     ca
 *   Right alloca redzone:    cb
 *   Shadow gap:              cc
 * ==30==ABORTING
 */
```
