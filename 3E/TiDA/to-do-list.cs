using System;
using System.Collections.Generic;

class Program
{
    static List<string> tasks = new List<string>();

    static void Main(string[] args)
    {
        while (true)
        {
            Console.WriteLine("Witaj w aplikacji To-Do List!");
            Console.WriteLine("1. Dodaj zadanie");
            Console.WriteLine("2. Usuń zadanie");
            Console.WriteLine("3. Wyświetl zadania");
            Console.WriteLine("4. Zakończ program");
            Console.Write("Wybierz opcję: ");

            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    AddTask();
                    break;
                case "2":
                    RemoveTask();
                    break;
                case "3":
                    ShowTasks();
                    break;
                case "4":
                    Console.WriteLine("Zamykanie programu...");
                    return;
                default:
                    Console.WriteLine("Nieprawidłowy wybór, spróbuj ponownie.");
                    break;
            }

            Console.WriteLine();
        }
    }

    static void AddTask()
    {
        Console.Write("Wprowadź zadanie do dodania: ");
        string task = Console.ReadLine();
        tasks.Add(task);
        Console.WriteLine("Zadanie dodane.");
    }

    static void RemoveTask()
    {
        Console.Write("Podaj numer zadania do usunięcia: ");
        ShowTasks();
        if (int.TryParse(Console.ReadLine(), out int index) && index >= 1 && index <= tasks.Count)
        {
            tasks.RemoveAt(index - 1);
            Console.WriteLine("Zadanie usunięte.");
        }
        else
        {
            Console.WriteLine("Nieprawidłowy numer zadania.");
        }
    }

    static void ShowTasks()
    {
        if (tasks.Count == 0)
        {
            Console.WriteLine("Brak zadań.");
            return;
        }

        Console.WriteLine("Lista zadań:");
        for (int i = 0; i < tasks.Count; i++)
        {
            Console.WriteLine($"{i + 1}. {tasks[i]}");
        }
    }
}
