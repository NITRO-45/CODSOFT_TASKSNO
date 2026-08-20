# CODSOFT Artificial Intelligence Internship

This repository contains the 3 tasks I completed during my **CODSOFT Artificial Intelligence Internship**.

## Tasks

### Task 1 - Rule-Based Chatbot

A simple college assistant chatbot made using Python.

The chatbot uses `if-elif-else` conditions and keyword matching to answer basic questions about:

* College timings
* Library
* Courses
* Exams
* Fees
* Help

**File:** `Task1_Rule_Based_Chatbot/chatbot.py`

---

### Task 2 - Movie Recommendation System

A simple movie recommendation system based on movie genres.

The program compares the genres of the selected movie with other movies and recommends movies having the most genres in common.

For example, if a movie has the genres:

```text
Sci-Fi, Action, Thriller
```

the program checks other movies for matching genres and gives them a similarity score.

**File:** `Task2_Movie_Recommendation/movie_recommendation.py`

---

### Task 3 - Face Detection

A simple face detection program using **OpenCV** and a pretrained **Haar Cascade classifier**.

The program takes an image, detects the faces in it, and draws a rectangle around each detected face.

**File:** `Task3_Face_Detection/face_detection.py`

**Input image:**

```text
Task3_Face_Detection/crowd.jpg
```

### Technologies Used

* Python
* OpenCV
* Haar Cascade
* Basic NLP concepts
* Content-based recommendation

## Folder Structure

```text
CODSOFT_TASKSNO/
│
├── README.md
│
├── Task1_Rule_Based_Chatbot/
│   └── chatbot.py
│
├── Task2_Movie_Recommendation/
│   └── movie_recommendation.py
│
└── Task3_Face_Detection/
    ├── face_detection.py
    └── crowd.jpg
```

## How to Run

First install OpenCV for Task 3:

```bash
pip install opencv-python
```

Then run any task using:

```bash
python Task1_Rule_Based_Chatbot/chatbot.py
```

```bash
python Task2_Movie_Recommendation/movie_recommendation.py
```

```bash
python Task3_Face_Detection/face_detection.py
```

## Internship

**CODSOFT - Artificial Intelligence Internship**

Completed 3 project tasks as part of the internship.
