import time

target_text = "suryansh pratap singh idiot and  you are stupid"
print(f"Target text: {target_text}")
print(target_text)

input("Press Enter to continue...")
start_time = time.time()

user_input = input("Please enter the target text exactly as shown above:\n")
end_time = time.time()

if user_input == target_text:
    print("Congratulations! You entered the text correctly.")
    time_taken = end_time - start_time
    print(f"Time taken: {end_time - start_time:.2f} seconds")

else:
    print("The entered text does not match the target text.")
