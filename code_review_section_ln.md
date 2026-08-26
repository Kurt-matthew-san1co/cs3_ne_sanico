### 

### **Annex C**

**Code Quality Assessment Worksheet**

**Section: 9-Neon						Score:\_\_\_\_\_\_\_\_\_\_\_\_**  
**C\# / Name: Kurt Matthew Sanico, Jamich Emmanuel Turao	Date: 26/08/2026**

**Instructions:**

**The problem: Search for a Number in a Sorted List**

**For example: Both algorithms could search:**   
numbers \= \[5, 12, 18, 23, 31, 47, 56, 68, 74, 90\]  
target \= 47

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| def linear\_search(numbers, target):    *for* i *in* range(len(numbers)):        *if* numbers\[i\] \== target:            *return* i    *return* \-1   | def binary\_search(numbers, target):    low \= 0    high \= len(numbers) \- 1     *while* low \<= high:        middle \= (low \+ high) // 2         *if* numbers\[middle\] \== target:            *return* middle        *elif* numbers\[middle\] \< target:            low \= middle \+ 1        *else*:            high \= middle \- 1     *return* \-1   |

## 

## 

## 

## 

## **Questions with Checklists**

### **1\. Efficiency**

Which algorithm is faster when the list of numbers is very large? Why?

The longer algorithm would be faster than the smaller one. Longer algorithms tend to split the problem into multiple parts, while shorter algorithms handle the entire package all at once without any pillows to soften the blow. Yes, Implementation 1 may look cute, petite, and organized, but it will struggle whenever you add too much to its load.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? | How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? |

**2\. Readability**

Which algorithm is easier to understand at first glance? What makes it clearer?

It would be the shorter code. The more words/characters/variables you need to comprehend within a single algorithm, the more confusing it becomes. Meanwhile, a shorter code can work in almost the same way and are easily more digestible than the paragraph long algorithm from Implementation 2.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? | How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process? |

### 

### **3\. Maintainability**

If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?

It would be Implementation 1. Having an easy-to-digest and short algorithm also almost always ensures that you can easily spot errors or mistakes in your code. On the other hand, Implementation 2 features more stuff: more loops, more variables, more everything. It would be a hassle to check every element. Although the troubleshooting process is eased up by built-in tips or auto-correction features in most IDEs, it would still save a bit of time to check your long code.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? | Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating? |

### 

### **4\. Testability**

Which algorithm is easier to test with different inputs? Why?

Implementation 1 works best in this type of scenario, as shorter algorithms are easier to test, having less paths and variables. With potentially fewer loops, the number of conditional inputs you can use is lessened. Also, just like I explained in a previous answer, longer algorithms are more complex, thus making it very difficult to isolate why an input failed.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? | Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear? |

### **5\. Reliability and Input Validation**

What should the algorithm check to avoid errors when receiving input from a user?

Verify whether the user input matches the wanted data type for the input. The algorithm should also use a "whitelist" to only allow certain characters (numbers) to be entered. The program should try to limit the input length to prevent the implementations from buffering or just straight up giving up.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Linear Search? | Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Binary Search? |

### 

### **6\. Final Answer**

Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.

Me and my partner have decided on choosing Implementation 1 as the superior implementation of code. It is easy to analyze, troubleshoot, test, and use overall. With the only major downside being its efficiency, this implementation stood out as a better choice with more pros than cons.
