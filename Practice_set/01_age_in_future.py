while True:
    nowyear = 2021
    try:
        age_or_YOB = int(input("Please Enter you age or year of birth: "))
    
        if age_or_YOB >= 0 and age_or_YOB <= 150:
            age = age_or_YOB
            if age >= 0 and age <= 100: 
                print(f"You will be 100 years old after {100 - age} years")
            else:
                print(f"You have already reached 100 years old {age - 100} years ago.")

            response = input('''Do you want to know what will be your age in upcoming year?
            If so please enter "y" else press any other key: ''')
            if response == "y" or response == "Y":
                try:
                    y = int(input("Please enter the year: "))
                    year = nowyear - age
                    print(f"You will be {y - year} years old in {y}")
                except exception as e:
                    print("You have entered invalid year")
        elif age_or_YOB >= 1850:
            year = age_or_YOB
            if year <= nowyear and year > (nowyear - 100):
                print(f"You will be 100 years old in {year + 100}")

                response = input('''Do you want to know what will be your age in upcoming year?
                If so please enter "y" else press any other key: ''')
                if response == "y" or response == "Y":
                    try:
                        y = int(input("Please enter the year: "))
                        print(f"You will be {y - year} years old in {y}")
                    except exception as e:
                        print("You have entered invalid year")

            elif year <= (nowyear-100):
                print(f"You have already reached 100 years old in {year + 100}")
            else:
                print("You are not born yet")
        elif age_or_YOB < 1850:
            print("You seem the oldest person alive.")
        else:
            print("Your input is not valid. Make sure you have entered valid year or age.")

    except Exception as e:
        print("Your input is not valid. Make sure you have entered valid year or age.")
    end = input("Please press 'e' to exit or press any other key to continue: ")
    if end == "e" or end == "E":
        print("****Thanks for using this program****")
        exit()
        