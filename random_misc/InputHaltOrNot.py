"""
Program that determines if an input program halts.
"""

class Program:
    """
    Class that represents a program.
    """
    def __init__(self, name, instructions):
        """
        Initializes a program.
        """
        self.name = name
        self.instructions = instructions
        self.instruction_pointer = 0
        self.halt = False
        
    def run(self):
        """
        Runs the program.
        """
        while not self.halt:
            self.step()
    
    def step(self):
        """
        Executes the next instruction.
        """
        instruction = self.instructions[self.instruction_pointer]
        if instruction == "halt":
            self.halt = True
        elif instruction == "nop":
            self.instruction_pointer += 1
        elif instruction == "jmp":
            self.instruction_pointer += 2
        else:
            self.instruction_pointer += 3
            
    def __str__(self):
        """
        Returns a string representation of the program.
        """
        return self.name
    
def main(): 
    
    # Read the input file.
    with open("InputHaltOrNot.txt") as file:
        lines = file.readlines()
    
    # Parse the input file.
    programs = []
    for line in lines:
        name, instructions = line.strip().split(": ")
        instructions = instructions.split(", ")
        programs.append(Program(name, instructions))
    
    # Run the programs.
    for program in programs:
        program.run()
    
    # Determine if the programs halt.
    halt = True
    for program in programs:
        if not program.halt:
            halt = False
    
    # Print the result.
    if halt:
        print("The programs halt.")
    else:
        print("The programs do not halt.")
        
if __name__ == "__main__":
    main()

