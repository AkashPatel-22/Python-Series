
#Match Case Statements
# -- the match/ case statements are an alternative to long chain of
# If..elif..else statements.

# 1. match = what you'r comparing.
# 2. case = the value or pattern to match against.
# 3. _ = wildcard (matches anything, like "default")



# example:- traffic light

color = input("enter color: ")

match color:
    case "red":
        print("STOP")
    case "green":
        print("GOO")
    case "yellow":
        print("LOOK")
    case _:
        print("wrong color")
            