def find_max(arr):
  maxi = arr[0]
  for num in arr:
    if num > maxi:
      maxi = num
  return maxi

test_list = [-3, 9, 7, 5]
print find_max(test_list)