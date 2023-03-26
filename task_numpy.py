from io import BytesIO
from PIL import Image
import numpy as np
import requests

# L1
# Replace all odd numbers in arr with -1
arr = np.arange(0, 10)
arr[arr % 2 == 1] = -1
print(arr)


# L2
# Insert np.nan values at 20 random positions in iris_2d dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='object')
iris_2d[np.random.randint(iris_2d.shape[0], size=20), np.random.randint(iris_2d.shape[1], size=20)] = np.nan
print(iris_2d)

# Get the positions of top 5 maximum values in a given array a
np.random.seed(100)
arr = np.random.uniform(1, 50, 20)
print(arr)
ind = np.argpartition(-arr, 5)[:5]
print(arr[ind])


# L3
# Find the duplicate entries (2nd occurrence onwards) in the given numpy array and mark them as True. First time occurrences should be False
np.random.seed(100)
arr = np.random.randint(0, 5, 10)
result = np.full(len(arr), True)
result[np.unique(arr, True)[1]] = False
print(result)

# Given an array of a non-continuous sequence of dates. Make it a continuous sequence of dates, by filling in the missing dates.
dates = np.arange(np.datetime64('2018-02-01'), np.datetime64('2018-02-25'), 2)
missing_dates = []
for date in dates:
    missing_dates.append(date)
    missing_dates.append(date + 1)
result = np.array(missing_dates)
print(result)

# Import the image from the following URL and convert it to a numpy array.
url = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
response = requests.get(url)
image_bytes = Image.open(BytesIO(response.content))
arr = np.asarray(image_bytes)
img = Image.fromarray(np.uint8(arr))
Image.Image.show(img)


# L4
# Find all the peaks in a 1D numpy array a. Peaks are points surrounded by smaller values on both sides
a = np.array([1, 3, 7, 1, 2, 6, 0, 1])
peaks = []
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] and a[i + 1] < a[i]:
        peaks.append(a[i])
print(peaks)

# Compute the counts of unique values row-wise.
np.random.seed(100)
arr = np.random.randint(1, 11, size=(6, 10))
value_count = [np.unique(row, return_counts=True) for row in arr]
result = []
for a, b in value_count:
    inner_result = []
    for i in np.unique(arr):
        if i in a:
            inner_result.append(int(b[a == i]))
        else:
            inner_result.append(0)
    result.append(inner_result)
print(result)

# Compute the one-hot encodings (dummy binary variables for each unique value in the array)
np.random.seed(101)
arr = np.random.randint(1, 4, size=6)
numbers = np.unique(arr)
result = np.zeros((arr.shape[0], numbers.shape[0]))
for i, k in enumerate(arr):
    result[i, k - 1] = 1
print(result)
