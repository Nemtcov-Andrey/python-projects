# Срезы ver.1.

# Дан список чисел:
# nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
# Программа выводит на экран шесть ответов:
# В первой строке первые пять элементов списка.
# Во второй строке весь список, кроме последних двух элементов.
# В третьей строке все элементы с чётными индексами.
# В четвёртой строке все элементы с нечётными индексами.
# В пятой строке все элементы в обратном порядке.
# В шестой строке все элементы списка через один в обратном порядке, начиная с последнего.

nums = [48, -10, 9, 38, 17, 50, -5, 43, 46, 12]
num = nums[:]

print(num[:5])    
print(num[:-2])   
print(num[::2])   
print(num[1::2])  
print(nums[::-1]) 
print(num[::-2])  
