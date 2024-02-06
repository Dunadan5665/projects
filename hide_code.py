def hide_characters(code, num_hide):
    hidden_code = "*" * num_hide + code[num_hide:]
    return hidden_code


code = "123456789123"
num_hide = 8
result = hide_characters(code, num_hide)
print(result)
