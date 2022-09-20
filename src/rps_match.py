def rps_match(str1, str2):
    win_map = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if check_valid_input(str1) and check_valid_input(str2):
        if str1 == str2:
            return "tie"
        elif win_map[str1] == str2:
            return str1
        else:
            return str2
    else:
        try:
            raise ValueError("Input was incorrect")
        except ValueError:
            print("Except Line of Error")
            raise

def check_valid_input(str):
    if str != "rock" and str != "scissors" and str != "paper":
        return False
    else:
        return True