class Token:
    def __init__(self, value_type, value):
        self.type = value_type
        self.value = value

def lexical_analysis(input_str):
    tokens = []
    index = 0

    while index < len(input_str):
        value = input_str[index]

        if value.isalnum() or value in "ϵ?.":
            tokens.append(Token("variables", value))
        elif value in "*+":
            tokens.append(Token("uni-operators", value))
        elif value == "|":
            tokens.append(Token("binary-operator", value))
        elif value == "(":
            tokens.append(Token("group_start", value))
        elif value == ")":
            tokens.append(Token("group_end", value))
        else:
            return("Error: Invalid input at position:", index + 1)
        
        index += 1

    return parser(tokens,input_str)

    

def parser(tokens,input_str):
    stack = []
    count=0

    
    for i in range(len(tokens)):
        if tokens[i].type == "variables":
            if tokens[i].value == "?" and count==0:
                    return "Error: Unexpected", tokens[i].value, "at", i
            count+=1
            pass
        elif tokens[i].type == "uni-operators":
            if i == 0 or tokens[i - 1].type in ["group_start", "binary-operator","uni-operators"] or tokens[i - 1].value == "?":
                return "Error: Unexpected", tokens[i].value, "at", i
        elif tokens[i].type == "binary-operator":
            if i == 0 or i == len(tokens) - 1 or tokens[i - 1].type in ["group_start", "binary-operator"] or \
                    tokens[i + 1].type in ["group_end", "uni-operators"]:
                return "Error: Unexpected", tokens[i].value, "at", i
        elif tokens[i].type == "group_start":
            stack.append(i)
        elif tokens[i].type == "group_end":
            if not stack:
                return "Error: Unmatched closing parenthesis at", i
            stack.pop()

    if stack:
        return "Error: Unmatched opening parenthesis at", stack[-1] + 1

    if count>0:
        return input_str
    else:
        return "Error: No variables"