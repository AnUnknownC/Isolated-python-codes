def factorial(number):
    if number == 0 or number == 1:
        return 1
    number *= factorial(number - 1)
    return number

def uniq_count(string):
    string = string.upper()
    div = 1
    res = []
    for i in string:
        if len(res) == 0 or i not in res:
            res.append(i)
    for i in range(len(res)):
        res[i] = string.count(res[i])
    for i in range(len(res)):
        div *= factorial(res[i])
    tot = factorial(len(string))//div
    return tot
    pass # good luck

# Example usage
input_string = "FZCvzWJoqlpKMRempkboraANuYi"
unique_count = uniq_count(input_string)
print(unique_count)