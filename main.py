# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))
print("This is a commit test")
print("This is a second test, adding a test branch to the repo")
# Run unit tests automatically
main(module='test_module', exit=False)