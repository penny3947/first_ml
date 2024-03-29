
###########
## NUMPY ##
###########

'''
#ndarray의 데이터 타입
import numpy as np
lst = [1,2,3,4]
arr1 = np.array(lst, np.int)
print(arr1)
arr2 = np.array(lst, np.str)
print(arr2)
arr3 = np.array(lst, np.float)
print(arr3)

'''
# ndim.0차원
import numpy as np
arr = np.array(5)
print(arr)
print(arr.ndim)


# ndim.1차원 : 벡터
import numpy as np
lst = [1, 2, 3, 4]
arr = np.array(lst)
print(arr)
print(arr.ndim)


# ndim.2차원 : 메트릭스
import numpy as np
lst = [[1, 2], [3, 4]]
arr = np.array(lst)
print(arr)
print(arr.ndim)
print("shape : ", arr.shape)


# ndim.3차원 : 텐서
import numpy as np
lst = [([1, 2], [3, 4])]
arr = np.array(lst)
print(arr)
print(arr.ndim)
print("shape : ", arr.shape)


# shape, size, dtype
import numpy as np
arr = np.zeros((3, 5, 2), dtype=np.int)
print(arr.ndim)
print("shape : ", arr.shape)
print("size : ", arr.size)
print("dtype : ", arr.dtype)
