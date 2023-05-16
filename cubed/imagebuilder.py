def replace_commas_with_newline(input_file, output_file):
    with open(input_file, "r") as f:
        s = f.read()
    count = 0
    new_s = ""
    for i in range(len(s)):
        if s[i] == ",":
            count += 1
            if count % 12 == 0:
                new_s += ",\n\t"
            else:
                new_s += s[i]
        else:
            new_s += s[i]
    with open(output_file, "w") as f:
        f.write(new_s)

input_file = "rubber_ducky2.c"
output_file = "output2.txt"
replace_commas_with_newline(input_file, output_file)