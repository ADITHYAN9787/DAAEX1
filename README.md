# DAAEX1
# Implementation and Performance Analysis of Interpolation Search

## 📌 Project Overview

This project implements the **Interpolation Search** algorithm and compares its performance with the **Binary Search** algorithm on sorted datasets of different sizes.

The objective is to analyze the execution time of both searching techniques and understand in which scenarios Interpolation Search outperforms Binary Search.

---

## 📖 Problem Statement

Given a **sorted array of uniformly distributed integers**, implement **Interpolation Search** to find the position of a target element.

Compare its performance with **Binary Search** using datasets of the following sizes:

- 1,000 elements
- 5,000 elements
- 10,000 elements
- 50,000 elements
- 100,000 elements

---

## 🎯 Objectives

- Implement Interpolation Search.
- Implement Binary Search.
- Measure and compare execution time.
- Analyze the efficiency of both algorithms.
- Observe the effect of increasing dataset size on performance.

---

## 🛠 Technologies Used

- C++
- Standard Template Library (STL)
- `<chrono>` library for execution time measurement

---

## 📂 Project Structure

```
├── interpolation_search.cpp
├── binary_search.cpp
├── performance_analysis.cpp
├── README.md
```

*(Modify the file names according to your project.)*

---

## ⚙️ Algorithms Used

### Interpolation Search

Interpolation Search estimates the probable position of the target based on the values in the array.

**Average Time Complexity:** `O(log log n)`  
**Worst Time Complexity:** `O(n)`  
**Space Complexity:** `O(1)`

Best suited for:
- Sorted arrays
- Uniformly distributed data

---

### Binary Search

Binary Search repeatedly divides the search interval into halves.

**Best Case:** `O(1)`  
**Average Case:** `O(log n)`  
**Worst Case:** `O(log n)`  
**Space Complexity:** `O(1)`

Best suited for:
- Any sorted array

---

## 📊 Performance Analysis

The algorithms were tested on sorted datasets of varying sizes.

| Dataset Size | Binary Search | Interpolation Search |
|--------------|--------------|----------------------|
| 1,000 | Measured | Measured |
| 5,000 | Measured | Measured |
| 10,000 | Measured | Measured |
| 50,000 | Measured | Measured |
| 100,000 | Measured | Measured |

*(Replace "Measured" with your actual execution times.)*

---

## ▶️ How to Run

### Compile

```bash
g++ performance_analysis.cpp -o search
```

### Execute

```bash
./search
```

or on Windows

```bash
search.exe
```

---

## 📈 Expected Outcome

- Interpolation Search performs faster than Binary Search when data is uniformly distributed.
- Binary Search provides consistent performance regardless of data distribution.
- For non-uniform datasets, Binary Search is generally more reliable.

---

## 📚 Learning Outcomes

Through this project, you will understand:

- Working of Interpolation Search
- Binary Search implementation
- Time complexity analysis
- Performance benchmarking in C++
- Importance of data distribution in search algorithms

---

## 🔮 Future Improvements

- Test with non-uniform datasets.
- Visualize execution times using graphs.
- Compare with Linear Search and Jump Search.
- Extend analysis to larger datasets.

---

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/ADITHYAN9787

---

## 📄 License

This project is intended for educational and academic purposes.
