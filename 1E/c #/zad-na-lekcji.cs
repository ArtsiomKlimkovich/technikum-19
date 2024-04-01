using System;
using System.Linq;

class Program
{
    public static void Main(string[] args)
    {
        Random r = new Random();
        int[] T = new int[10];
        // zad 1
        // int max = 0;
        // for (int i = 0; i < T.Length; ++i){
        //     T[i] = r.Next(1, 20);
        // }
        // for (int i = 0; i < T.Length; ++i){
        //     Console.Write (T[i] + " ");
        // }
        // // Console.Write("max number is " + T.Max());
        // for (int i = 0; i < T.Length; ++i){
        //     if (T[i] > max){
        //         max = T[i];
        //     }
        // }
        // Console.Write("max number is " + max);

        //zad 2
        // int min = 20;
        // for (int i = 0; i < T.Length; ++i){
        //     T[i] = r.Next(1, 20);
        // }
        // for (int i = 0; i < T.Length; ++i){
        //     Console.Write (T[i] + " ");
        // }
        // // Console.Write("max number is " + T.Max());
        // for (int i = 0; i < T.Length; ++i){
        //     if (T[i] < min){
        //         min = T[i];
        //     }
        // }
        // Console.Write("min number is " + min);

        //zad 3
        // int max = 0;
        // int maxcount = 0;
        // for (int i = 0; i < T.Length; ++i){
        //     T[i] = r.Next(1, 20);
        // }

        // for (int i = 0; i < T.Length; ++i){
        //     Console.Write (T[i] + " ");
        // }
        // for (int i = 0; i < T.Length; ++i){
        //     if (T[i] > max){
        //         max = T[i];
        //     }
        // }
        // for (int i = 0; i < T.Length; ++i){
        //     if (T[i] == max){
        //         maxcount++;
        //     }
        // }
        // Console.Write("max num appears " + maxcount + " times");

        //zad 5
        // int max = 0;
        // int min = 20;
        // for (int i = 0; i < T.Length; ++i){
        //     T[i] = r.Next(1, 20);
        // }
        // for (int i = 0; i < T.Length; ++i){
        //     Console.Write (T[i] + " ");
        // }
        // for (int i = 0; i < T.Length; ++i){
        //     if (T[i] > max){
        //         max = T[i];
        //     }
        // }
        // for (int i = 0; i < T.Length; ++i){
        //     if (T[i] < min){
        //         min = T[i];
        //     }
        // }

        // Console.WriteLine("max - min = " + (max-min));

        //zad 6
        // int sum = 0;
        // for (int i = 0; i < T.Length; ++i){
        //     T[i] = r.Next(1, 20);
        // }

        // for (int i = 0; i < T.Length; ++i){
        //     Console.Write (T[i] + " ");
        // }

        // for (int i = 0; i < T.Length; ++i){
        //     sum += T[i];
        // }
        // Console.Write("sum of array --> " + sum);


        //zad 7
        // int sum = 0;
        // for (int i = 0; i < T.Length; ++i){
        //     T[i] = r.Next(1, 20);
        // }

        // for (int i = 0; i < T.Length; ++i){
        //     Console.Write (T[i] + " ");
        // }
        // for (int i = 0; i < T.Length; ++i){
        //     sum += T[i];
        // }
        // double avg = sum / T.Length;
        // Console.Write("avarage num of array -->" + avg);

        //zad 8
        int even = 0;
        int odd = 0;
        for (int i = 0; i < T.Length; ++i){
            T[i] = r.Next(1, 20);
        }

        for (int i = 0; i < T.Length; ++i){
            Console.Write (T[i] + " ");
        }
        for (int i = 0; i < T.Length; ++i){
            if (T[i] % 2 == 0){
                even++;
            }
            else{
                odd++;
            }
        }
        if (even > odd){
            Console.Write("Even nums is more");
        }
        else if (odd > even){
            Console.Write("Odd nums is more");
        }
        else{
            Console.Write(" even and odd is equal");
        }




    }
}