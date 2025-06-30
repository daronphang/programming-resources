## Sprout method

When you need to add a feature to a system and you can't get tests around method, and it can be formulated completely as new code, write the code in a new method instead of writing the code inline. Call it from the places where the new functionality needs to be. You can take the following steps for using Sprout method:

1. Identify where you need to make your code change
2. If the change can be formulated as a single sequence of statements in one place in a method, write down a call for a new method that will do the work involved and then comment it out
3. Determine what local variables you need from the source method, and make them arguments to the call
4. Determine whether the sprouted method will need to return values to source method. If so, change the call so that its return value is assigned to a variable
