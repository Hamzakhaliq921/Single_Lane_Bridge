# 🛣️ Deadlock-Free Synchronization for a Single Lane Bridge

**Course:** Operating Systems (CS-212)  
---

## 📌 Project Overview

This project simulates a real-world concurrency problem known as the **Single Lane Bridge Problem**, where vehicles (farmers) from two directions attempt to cross a single-lane bridge without collision or deadlock.

Each farmer is modeled as an independent **POSIX thread*, and access to the bridge is controlled using **mutex locks and synchronization techniques**. The system ensures:

- Deadlock-free execution  
- Starvation prevention  
- Mutual exclusion  
- Fair access from both directions  

A **GUI-based visualization** displays real-time thread states and bridge activity.

---

## 🎯 Project Objectives

- Demonstrate real-world **process and thread synchronization** using Python.
- Implement **mutual exclusion** for safe access to the single-lane bridge.
- Demonstrate the use of **semaphores and locks** for controlling shared resources.
- Implement **deadlock avoidance** through controlled bridge access.
- Reduce **starvation** by managing access between North and South directions.
- Visualize **concurrent thread behavior** using a Tkinter-based GUI.
- Demonstrate important Operating Systems concepts including **critical sections, synchronization,    mutual exclusion, and resource sharing**.
- Provide both **graphical and console-based simulations** for observing thread execution and         synchronization.
---

## ⚙️ Key Functionalities

### 🧵 Thread Simulation
- Northbound and Southbound farmers represented as POSIX threads (`pthread`)

### 🔐 Synchronization
- Mutex locks control bridge access
- Only one direction allowed at a time

### 🚫 Deadlock Prevention
- Direction-based access control ensures no circular wait occurs

### ⚖️ Starvation Prevention
- Cycle-based fairness mechanism ensures both directions get equal access

### ⏱️ Realistic Behavior
- Random delays simulate real-world crossing time and waiting

### 🖥️ GUI Visualization
- Real-time display of:
  - Waiting farmers
  - Crossing farmers
  - Crossed farmers
- Bridge status:
  - Free
  - Occupied (North/South direction)
- User controls:
  - Number of farmers
  - Starvation threshold

---

| Documentation & Reporting | All Members |

---

## 🖥️ Tech Stack

- **Language:** Python 3
- **Threading:** Python threading module
- **Operating System:** Windows / Linux / macOS
- **Synchronization:** Semaphores and Locks (threading.Semaphore, threading.Lock)
- **GUI Toolkit:** Tkinter
- **Simulation:** Multithreaded Single-Lane Bridge Simulation
- **Core Concepts:** Mutual Exclusion, Critical Sections, Thread Synchronization, Deadlock Avoidance, Starvation Prevention
---

## 📷 Project Concept

- Two villages (North Tunbridge & South Tunbridge)
- One shared single-lane bridge
- Farmers (threads) must cross safely without conflict

---

## 🚀 Learning Outcomes

- Understanding of concurrency in Operating Systems
- Practical implementation of thread synchronization
- Handling deadlocks and starvation scenarios
- GUI integration with system-level programming

---

## 📜 License

This project is created for academic purposes under Bahria University coursework.

---
