class Main:
    def handle(self, input_str):
        """
        This method should parse each input and assign it into different variables.

        The value of the function parameter "input_str" will be of the format - "<COMMAND_NAME_1> <ARG1> <ARG2> .. <ARG N>".
        We split the string and retrieve the input data appropriately into the variable `inputs_for_one_command`.

        Main.handle() will be called in a loop for each command input.

        For example: If the inputs are:
          "PLACE_ORDER 101 Apple 5"
          "PLACE_ORDER 101 Orange 5"
          "TOTAL_COST 101"

        Main.handle is called thrice as follows respectively:

          Main.handle("PLACE_ORDER 101 Apple 5")
          Main.handle("PLACE_ORDER 101 Orange 5")
          Main.handle("TOTAL_COST 101")
        """
        inputs_for_one_command = input_str.strip().split(" ")
        command = inputs_for_one_command[
            0
        ]  # This value holds the command name each time it is called.
        print(command)  # Will print the command Ex: "PLACE_ORDER" or "TOTAL_COST"

        if len(inputs_for_one_command) > 1:
            arg1 = inputs_for_one_command[
                1
            ]  # This value holds the first argument value.
            print(arg1)  # Will print the first argument to the command Ex: "101"

        # TODO: Implement logic to handle each command here and print the respective output
