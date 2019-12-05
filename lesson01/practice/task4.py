# При условии что процент добавляется в телу депозита.
def bank(deposit_amount, number_years, percent):
    amount = deposit_amount
    for year in range(1, number_years + 1):
        amount *= 1 + percent/100

    return round(amount, 2)

print(bank(1000, 10, 10))
print(bank(10000, 5, 5))
print(bank(3000, 3, 2))
