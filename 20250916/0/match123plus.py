a = int(input())
match a:
    case 1:
        print("один")
    case 2:
        print("два")
    case 3:
        print("три")
    case n if n % 2 == 0:
        print("четное")
    case q if 1:
        print(q, "-- это много")
