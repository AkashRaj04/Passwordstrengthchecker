Password strength checker coded using python.

Takes a password as input from user and returns a score indicating its strength.

It uses a global variable x to keep track of how many different character classes the password contains (uppercase, lowercase, digit, and special character).

For each character class present in the password, the function increments the score and updates x.

The function then checks the length of the password and awards additional points for longer passwords.

Reads a list of common passwords from the file "common.txt" and checks if the given password is in that list.

If the password is too common, it prints a message indicating it to be weak.
