"""
Problem 1: function and control
"""


def calculate(min, max, step):
    total = 0
    if type(min) == int and type(max) == int and type(step) == int:
        if max > min and step > 0:
            for i in range(min, max+1, step):
                total += i
    else:
        print("非整數")

    print(total)


calculate(1, 3, 1)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2)  # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2)  # 你的程式要能夠計算 -1+1，最後印出 0


"""
Problem 2: dictionary and list
"""


def avg(data):
    employees_lst = data['employees']
    salary_sum = 0
    count = 0
    for employee in employees_lst:
        if not employee['manager']:
            salary_sum += employee['salary']
            count += 1
    print(salary_sum/count)


avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": False
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": True
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": False
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": False
        }
    ]
})  # 呼叫 avg 函式


"""
Problem 3
"""


def func(a):
    """ a是multipy()的環境變數"""
    def multipy(x, y):
        print(a + (x * y))
    return multipy  # 在這邊若用print需要呼叫函數+()，但x,y是multipy裡面的參數，func層裡無定義會噴錯


func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


"""
Problem 4
"""

# Solution 1 : O(N^2)
# def maxProduct(nums):
#     if len(nums) >= 2:
#         max_product = -float('inf')
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] * nums[j] > max_product:
#                     max_product = nums[i] * nums[j]
#         print(max_product)
#     else:
#         print("列表筆數不足2")

# Solution 2:
def maxProduct(nums):
    if len(nums) >= 2:
        max_product = -float('inf')
        print(max_sort(nums, max_product))
    else:
        print('資料筆數不足2')


def max_sort(nums, max_product):
    if len(nums) <= 1:
        return max_product
    pivot = nums.pop()

    for num in nums:
        if num * pivot > max_product:
            max_product = num * pivot
    return max_sort(nums, max_product)

# Solution 3 & 4:
# def maxProduct(nums):
#     if len(nums) >= 2:
#         sorted_nums = merge_sort(nums)
#         if sorted_nums[-1] * sorted_nums[-2] > sorted_nums[0] * sorted_nums[1]:
#             print(sorted_nums[-1] * sorted_nums[-2])
#         else:
#             print(sorted_nums[0] * sorted_nums[1])
#     else:
#         print('資料筆數不足2')


# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums.pop()
#
#     smaller_lst = []
#     greater_lst = []
#
#     for num in nums:
#         if num < pivot:
#             smaller_lst.append(num)
#         else:
#             greater_lst.append(num)
#     return quick_sort(smaller_lst) + [pivot] + quick_sort(greater_lst)
#
#
# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#
#     mid = len(nums) // 2
#
#     left_lst, right_lst = merge_sort(nums[:mid]), merge_sort(nums[mid:])
#
#     return merge(left_lst, right_lst)
#
#
# def merge(left_lst, right_lst):
#     sorted_lst = []
#     left_pointer = 0
#     right_pointer = 0
#     while left_pointer < len(left_lst) and right_pointer < len(right_lst):
#         if left_lst[left_pointer] < right_lst[right_pointer]:
#             sorted_lst.append(left_lst[left_pointer])
#             left_pointer += 1
#         else:
#             sorted_lst.append(right_lst[right_pointer])
#             right_pointer += 1
#
#     sorted_lst.extend(left_lst[left_pointer:])
#     sorted_lst.extend(right_lst[right_pointer:])
#     return sorted_lst


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2])  # 得到 10


"""
Problem 5
"""

# Solution 1: O(n^2)
# def twoSum(nums, target):
#     for i in range(len(nums)-1):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# Solution 2 :
def twoSum(nums, target):
    pivot_index = len(nums) - 1
    pivot = nums.pop()

    for i in range(len(nums)):
        if pivot + nums[i] == target:
            return [i, pivot_index]
    return twoSum(nums, target)


result=twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9


"""
Problem 6
"""


def maxZeros(nums):
    max_count = 0
    count = 0
    is_consecutive = 0  # 0 for off 1 for on
    for num in nums:
        if num == 0 and is_consecutive == 0:
            count = 0   # reset
            count += 1
            is_consecutive = 1  # turn on
        elif num == 0 and is_consecutive == 1:
            count += 1
        else:
            is_consecutive = 0  # turn off
            if count > max_count:
                max_count = count
    if count > max_count:
        max_count = count
    print(max_count)


maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3