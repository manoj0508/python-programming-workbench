def main()-> None:
    empl_list= [45000,80000,60000,35000]

    cutoff_salary= int(input("Enter the filter salary amount : "))

    filter_salary = lambda salary : salary> cutoff_salary

    revised_salary = list(filter(filter_salary,empl_list))
    print(revised_salary)







if __name__ == "__main__":
    main()