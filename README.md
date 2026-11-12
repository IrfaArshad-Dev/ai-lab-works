# 🤖 AI Lab Works

My lab work for the **Artificial Intelligence** course at Riphah International University (BS Software Engineering). The repository goes step by step from Python basics to search algorithms, intelligent agents, logic programming and machine learning.

## 🧭 What's Inside

| Lab | Topic | File |
|-----|-------|------|
| 1 | Introduction to AI, Python and Google Colab (report) | `Lab 1.pdf`, `LAB 1 task.py` |
| 2 | Input, variable swapping, string counting, assignment operators, lists | `Lab 2 Tasks.py` |
| 3 | Conditional statements (`if / elif / else`), odd or even, bonus calculator | `lab 3.py` |
| 4 | Lists, sets, tuples and dictionaries | `Lab 4.py` |
| 5 | `for` loops, nested loops, searching with `for ... else` | `LAb 5 task.py` |
| 6 | NumPy arrays: dimensions, `arange`, array arithmetic, sum, average, max, min | `LAB 6 TASKS.py` |
| 7 | NumPy matrices: multiplication, transpose, indexing, copy vs view, concatenation | `Lab 7.py` |
| 8 | Graph search: **Breadth First Search (BFS)** and **Depth First Search (DFS)** | `Lab 8.py` |
| 9 | **Simple reflex agent** in a two-room vacuum cleaner world | `LAB 9.py`, `Lab 9 task 1.pdf` |
| 10 | **Prolog**: facts, queries, variables and rules (report) | `Lab 10.pdf` |
| 11 | Machine learning on the Iris dataset: preprocessing, KNN and decision tree | `lab 11.zip` |
| 12 | **K-Nearest Neighbors written from scratch** and tested on Iris | `Lab 12.py.py` |

## 🔍 Highlights

### Lab 8: BFS and DFS
Both searches run on the same binary tree. BFS uses a queue (FIFO) and visits level by level, while DFS uses recursion and goes deep into one branch before backtracking.

### Lab 9: Vacuum Cleaner Agent
A `VacuumEnvironment` class holds the state of rooms A and B, and a `SimpleReflexAgent` chooses its action from the current percept (location and whether the room is dirty):
- Dirty room → `Suck`
- Clean room in A → `Move Right`
- Clean room in B → `Move Left`

The program also counts the dirty rooms after each step, and the report walks through several starting conditions.

### Lab 10: Prolog
Facts such as `likes(ali, apples).`, queries with variables like `likes(Who, apples)`, and a rule that makes two people friends when both enjoy cricket.

### Lab 11: Machine Learning with scikit-learn (`lab 11.zip`)
- `task1.py`: loads the Iris dataset into a pandas DataFrame and preprocesses it with `SimpleImputer`
- `task2.py`: scales the features with `StandardScaler`, then trains a `KNeighborsClassifier`
- `task3.py`: trains a `DecisionTreeClassifier` and measures its accuracy
- `practice.py`: logistic regression on the breast cancer dataset, with median imputation, scaling and a confusion matrix

### Lab 12: KNN from Scratch
A custom `KNN` class with its own Euclidean distance function. It is trained on an 80/20 train-test split of Iris and compared for **k = 1, 3, 5 and 7** using accuracy.

## 🛠️ Tech Used
- **Language:** Python 3
- **Libraries:** NumPy, pandas, scikit-learn, Matplotlib, Seaborn
- **Other:** SWI-Prolog, Google Colab, Spyder / VS Code

Every lab file runs on its own. Labs 1 to 9 need only Python (labs 6 and 7 also need NumPy). The Prolog work in Lab 10 needs [SWI-Prolog](https://www.swi-prolog.org/).

## 🧠 Concepts Covered
Python fundamentals · data structures · NumPy · uninformed search (BFS, DFS) · intelligent agents · logic programming · data preprocessing · classification (KNN, decision tree, logistic regression) · model evaluation

## 👩‍💻 Author
**Irfa Arshad** | [GitHub](https://github.com/IrfaArshad-Dev)

*BS Software Engineering, Riphah International University*
