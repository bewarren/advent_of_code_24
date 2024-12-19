with open('input.txt', 'r') as file:
    content = file.read()

registers, program = list(content.split('\n\n'))



register_vals = ["A", "B", "C"]
register_dict = {}

for i, val in enumerate(registers.split("\n")):
    register_dict[register_vals[i]] = int(val.split(":")[1])

print(register_dict)
print('')


program_instructions = [int(x) for x in program.split(":")[1].split(",")]

print(program_instructions)


def get_combo_operand(operand):
    if operand >=0 and operand<=3:
        return operand 
    
    elif operand == 4:
        return register_dict['A']

    elif operand == 5:
        return register_dict["B"]
    
    elif operand == 6:
        return register_dict['C']
    
    else:
        return "Error"


out = []
def perform_operation(instruction_pointer, opcode, operand):
    if opcode == 0:
        register_dict['A'] = int(register_dict['A'] / (2**get_combo_operand(operand))) 
        return instruction_pointer + 2
    
    elif opcode == 1:
        register_dict['B'] = register_dict["B"] ^ operand
        return instruction_pointer + 2

    elif opcode == 2:
        register_dict['B'] = get_combo_operand(operand) % 8
        return instruction_pointer + 2

    elif opcode == 3:
        if register_dict['A'] == 0:
            return instruction_pointer + 2
        else: 
            return operand
        
    elif opcode == 4:
        register_dict['B'] = register_dict['B'] ^ register_dict['C']
        return instruction_pointer + 2

    elif opcode == 5:
        # output this? 
        out.append(get_combo_operand(operand) % 8)
        return instruction_pointer + 2
    
    elif opcode == 6:
        register_dict['B'] = int(register_dict['A'] / (2**get_combo_operand(operand))) 
        return instruction_pointer + 2
    
    elif opcode == 7:
        register_dict['C'] = int(register_dict['A'] / (2**get_combo_operand(operand))) 
        return instruction_pointer + 2 
    else:
        return instruction_pointer + 2


instruction = 0
while instruction != len(program_instructions):
    
    instruction = perform_operation(instruction, program_instructions[instruction], program_instructions[instruction+1])

print(register_dict)
print(",".join(list(map(str, out))))