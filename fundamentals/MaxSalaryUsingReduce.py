from functools import reduce

def main()-> None:
    empl_list = [45000, 80000, 60000, 35000]
    max_salary_function = lambda a, b: a if a > b else b
    max_salary = reduce(max_salary_function,empl_list)
    print("Maximum Salary: ", max_salary)


if __name__ == "__main__":
    main()