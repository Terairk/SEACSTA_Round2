def strongweak(points):
    if points == 5:
        return "Strong"
    elif points > 2 and points < 5:
        return "Medium"
    else:
        return "Weak"

strongweak(4)
strongweak(3)
