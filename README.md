# 🧬 Single Inheritance in Python

## 📌 Description

This Python program demonstrates the concept of **Single Inheritance** in Object-Oriented Programming (OOP).
Class `B` inherits the properties and methods of class `A`, allowing objects of `B` to access methods from both classes.

---

## 🚀 Features

* Demonstrates **inheritance** in Python
* Shows method access from parent and child classes
* Uses a static `main()` method similar to Java style

---

## 🛠️ How It Works

### 1️⃣ Parent Class `A`

Contains:

* `method1()`
* `method2()`

### 2️⃣ Child Class `B`

```python id="x9r4pl"
class B(A)
```

👉 `B` inherits all methods of class `A`

Also contains:

* `method3()`
* `method4()`

### 3️⃣ Main Class `Inh1`

* Creates object of class `B`
* Calls:

  * inherited methods (`method1`, `method2`)
  * own methods (`method3`, `method4`)

---

## 💻 Code

```python id="q4m8zx"
class A:
    def method1(self):
        print("Inside method 1")

    def method2(self):
        print("Inside method 2")


class B(A):   # Inheriting class A
    def method3(self):
        print("Inside method 3")

    def method4(self):
        print("Inside method 4")


class Inh1:
    @staticmethod
    def main():
        obj = B()
        obj.method1()
        obj.method2()
        obj.method3()
        obj.method4()


# Calling main method
Inh1.main()
```

---

## ▶️ Output

```id="r7k2mv"
Inside method 1
Inside method 2
Inside method 3
Inside method 4
```

---

## 🧠 Key Concept

### ✔ Inheritance

Inheritance allows one class to acquire properties and methods of another class.

```python id="n6x3qa"
class B(A)
```

👉 `A` = Parent/Base class
👉 `B` = Child/Derived class

---

## 📚 Concepts Used

* Class & Object
* Single Inheritance
* Method calling
* Static method

---

## 🎯 Advantages of Inheritance

* Code reusability
* Reduces duplication
* Improves maintainability
* Supports hierarchical relationships

---

## 🔧 Future Improvements

* Add constructor inheritance
* Demonstrate method overriding
* Add multilevel inheritance
* Use `super()` method

---

## 📄 License

This project is open-source and free to use.
