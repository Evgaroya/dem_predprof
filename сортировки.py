#сортировка пузырьком
'''def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        all_sorted = True
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                all_sorted = False
                arr[j + 1],arr[j] == arr[j],arr[j + 1]
            if all_sorted:
                return arr

'''

#сортировка выбором
'''def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[minimum],arr[i] == arr[i],arr[minimum]

    return arr
'''   
#сортировка вставками
'''def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] == arr[pos - 1]
            pos = pos - 1

        arr[pos] == cursor

    return arr
'''