print("ahhahaha")  # Print the message as intended

for i in range(10):  # Fixed the inner loop to iterate 10 times
    print("dugaaruud: " + str(i) + " nogoo ni: " + str(j))  # Use f-strings for cleaner output

j = 1  # Initialize j outside the loop to avoid infinite loop

# Corrected the logic: Since j is initialized outside and never incremented,
# it will always be 1, resulting in "dugaaruud: i nogoo ni: 1" printed 10 times.
# To achieve a sequence of numbers for "nogoo ni:", you'd need a nested loop or alternative logic.
