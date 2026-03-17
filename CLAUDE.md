Some functions are supposed to be defined in logic_utils.py, but right now they are in app.py.
Let's move get_range_for_difficulty, parse_guess, check_guess, and update_score into app.py where it should be.

Then, without editing any existing comments, make the changes where there are comments on issues in the code. Then, write new comments under the change, for example # Fixed blah blah blah.

For each change, I want you to explain the change and why we are doing the change.



Additional things to change:

When we change the difficulty, we want it to make a new game based on that difficulty.

The final score isn't being calculated properly. 

Make sure the debug window captures our new 0-100 score system.