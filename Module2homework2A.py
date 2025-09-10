#calling the function
def minutes_to_hours_and_minutes():
    """
Anita Soffer
    1. Input how many minutes
    2. convert minutes to hours
    3. find the remainder (remaining_minutes)
    4. print hours and minutes

    """
    minutes = (int(input ("How many minutes? "))) #asking the user how many minutes ( the input)
    hours = (minutes // 60) # finding the whole number of hours- divide minutes by 60
    remaining_minutes = (minutes % 60) # finding the remaining minutes
    # then printing the reponse to the user in hours and minutes
    print ( "The answer is " , hours , "hours and", remaining_minutes, "minutes" )
    #calling the function again to close
minutes_to_hours_and_minutes()
    
    
