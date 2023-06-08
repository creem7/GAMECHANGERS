def generate_even_numbers(start, end):
    even_numbers = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


start_even_num = 4
end_even_num = 30
even_numbers = generate_even_numbers(start_even_num, end_even_num)
print(even_numbers)
