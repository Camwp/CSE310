import random

message = "Hello, World!"
shuffled = ''.join(random.sample(message, len(message)))

print(f"Shuffled: {shuffled}")
print(f"Original: {message}")
