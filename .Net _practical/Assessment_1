using System;
using System.Collections.Generic;
using System.Linq;

class Student
{
    public int StudentId;
    public string Name;
    public string Department;
    public int Marks;
}

class Program
{
    static List<Student> students = new List<Student>();

    static void Main()
    {
        int choice;

        do
        {
            Console.WriteLine("\n--- Student Management System ---");
            Console.WriteLine("1. Add Student");
            Console.WriteLine("2. Display All Students");
            Console.WriteLine("3. Display Name & Department");
            Console.WriteLine("4. Students with Marks > 75");
            Console.WriteLine("5. Students from Specific Department");
            Console.WriteLine("6. Sort Students by Marks (Descending)");
            Console.WriteLine("7. Display Top Scorer");
            Console.WriteLine("0. Exit");
            Console.Write("Enter your choice: ");
            choice = Convert.ToInt32(Console.ReadLine());

            switch (choice)
            {
                case 1: AddStudent(); break;
                case 2: DisplayAll(); break;
                case 3: DisplayNameDept(); break;
                case 4: MarksAbove75(); break;
                case 5: StudentsByDepartment(); break;
                case 6: SortByMarks(); break;
                case 7: TopScorer(); break;
            }

        } while (choice != 0);
    }

    static void AddStudent()
    {
        Student s = new Student();

        Console.Write("Enter Student ID: ");
        s.StudentId = Convert.ToInt32(Console.ReadLine());

        Console.Write("Enter Name: ");
        s.Name = Console.ReadLine();

        Console.Write("Enter Department: ");
        s.Department = Console.ReadLine();

        Console.Write("Enter Marks: ");
        s.Marks = Convert.ToInt32(Console.ReadLine());

        students.Add(s);
        Console.WriteLine("Student added successfully!");
    }

    static void DisplayAll()
    {
        foreach (var s in students)
        {
            Console.WriteLine($"{s.StudentId} {s.Name} {s.Department} {s.Marks}");
        }
    }

    static void DisplayNameDept()
    {
        foreach (var s in students)
        {
            Console.WriteLine($"{s.Name} - {s.Department}");
        }
    }

    static void MarksAbove75()
    {
        var result = students.Where(s => s.Marks > 75);
        foreach (var s in result)
        {
            Console.WriteLine($"{s.Name} {s.Marks}");
        }
    }

    static void StudentsByDepartment()
    {
        Console.Write("Enter Department: ");
        string dept = Console.ReadLine();

        var result = students.Where(s => s.Department.Equals(dept, StringComparison.OrdinalIgnoreCase));
        foreach (var s in result)
        {
            Console.WriteLine($"{s.Name} {s.Marks}");
        }
    }

    static void SortByMarks()
    {
        var result = students.OrderByDescending(s => s.Marks);
        foreach (var s in result)
        {
            Console.WriteLine($"{s.Name} {s.Marks}");
        }
    }

    static void TopScorer()
    {
        var top = students.OrderByDescending(s => s.Marks).FirstOrDefault();
        if (top != null)
            Console.WriteLine($"Top Scorer: {top.Name} - {top.Marks}");
    }
}
