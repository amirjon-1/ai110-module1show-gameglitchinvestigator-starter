# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

1) The hint was indeed backwards. It was saying go lower even though the answer was higher. I expect it to say higher if I enter a number less than the answer. 

2) Even though easy mode says the range is 1-20, the text on the website still says 1-100 which can confuse the user. The secret number is not even within this range either way. I would expect it to pressent correct information.

3) The history is very buggy. It works differently for even and odd cases and doesn't keep track correctly. 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

 I used Copilot. The AI was able to fix the checkGuess function which was a pretty simple fix for any programmer so I was able to verify it quickly, But what it did was comment, refactor and write edge cases which is much faster than your average developer. 
 It was correctly identifying the even attempy type error, but the fix it was offering was way too complex, so I told it to keep it simple and fix it in a easier way. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

I asked CoPilot to generate test cases and ran that. I did both manual and program test cases, where I tested multiple numbers to see if the check guessing functinality worked depending on if my guess was higher or less than the secret number. AI helped design the tests after it fixed the error, which was nice. 

When it created the test files, there were quite some errors. I think I shoud have given it more context regarding what checkGuess returns, but it was comparing a string against a tuple, not knowing checkGuess returned a tuple. So I managed to fix that after rejecting the original test case that Copilot wrote. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---
The number kept changing because Streamlit reruns the script on every interaction so it was just generating a new secret after every guess. 

Streamlit is like a document that refreshes each time you type something, and the session state that perserves data between interactions. 

I wrapped the secret generation in a check so it only runs when the key doesn't already exist in session state, preventing it from regenerating on every rerun.


## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
