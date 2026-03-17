# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game had 3 difficulty modes: Easy, Normal, and Hard. There was a box to input our guess, and a submit button, as well as a hint checkbox that told us whether our guess was higher or lower than the secret number. Most importantly for debugging, there was a debugging box that told us firsthand the secret number, how many attempts we have done, and a list of every guess we have made so far.

  There were many things wrong with the game at first. The difficulty logic was wrong, the hints did not give point the user in the right direction. However, despite these bugs the game did "work", just the logic was messed up and the game itself didn't play the way it was meant to be played.

- List at least two concrete bugs you noticed at the start  
  -The Normal difficulty is harder than the hard difficulty because the target number is between 1-100, while in the hard difficulty the range is 1-50.
  -When we are at an odd numbered attempt, it tells us that the target number is higher or lower than the number we guessed even though it is not.
  -The new game button does not work, it just keeps telling us the game is over and that we should start a new game, however in the debugging info window it does show us that the number of attempts we have has reset and that the secret number is also new each time we click new game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used Claude Code on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - It correctly gave me pointers on the lines in the program that changed what functions, for example which line makes the default score 0. I tested whether the lines it suggested actually did what Claude said it did by changing some values and seeing if that change reflects in the streamlit. Claude was really good at doing this.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - It incorrectly gave me the suggestion to floor the score at 0, so that it only moved when we guessed the correct number, which is not the way to track the score that we want, because our score will always either be 0 or 5.
    I verified this by just playing a round of the game, and realized that the suggestion Claude gave me was not the logic we wanted. This made me realize that the AI thinks too naive at times and does not stop to consider the user's experience, in this case the correct tracking of the user's score.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I asked Claude to write a test for it inside test_game_logic.py, then I tested the function myself within the streamlit app.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I had Claude write a test that tested whether pressing the "New Game" button actually worked and reset our score, attempts, and used a new secret number. I ran it, it passed. To make sure, I ran the streamlit app and tested the button and it worked. This told me that the fix we made on this function worked.
- Did AI help you design or understand any tests? How?
Yes, it helped me both design and understand each test, it helped me plan each test's inputs, expected outputs, as well as how we are able to test functions like a button working properly.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The line "secret = random.randint(low,high) was ran every time the user interacted with the app, whether it be a button, typing in a text box, or selecting from a dropdown.This line changes the secret number to a random new one. This change was silent and so the hint the user got would be inaccurate.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
If something needs to be persistent across interactions for example the score and more importantly the secret number in this case, it goes in as a session state. In streamlit, every interaction makes your app rerun from line 1, called a rerun. We can fix this using session state for the variables we need to be persistent.
- What change did you make that finally gave the game a stable secret number?
The fix was to wrap it inside this if statement: "if "secret" not in st.session_state". The if check makes it so the secret is only generated once and every rerun just reuses the same value.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
I want to use test cases in the future, where I will ask Claude to help me build a useful test case in a separate tests.py just like test_game_logic.py. I will then use these tests for every bug I encountered and made changes to fix.
- What is one thing you would do differently next time you work with AI on a coding task?
I think I could work on debugging code alongside Claude instead of searching for bugs and wasting time writing insie CLAUDE.md very rudementary bugs that it could spot itself. This way, I can focus on more hidden bugs that lay layers deep into the app.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project has taught me about test cases and how we can use AI to help understand, make sure functions we have debugged have been successfully debugged, to make sure that our AI generated code works. It's taught me that although AI is capable, it makes mistakes in situations where human interaction is what makes a function work.