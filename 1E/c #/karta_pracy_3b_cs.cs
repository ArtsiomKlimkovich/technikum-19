using System;
					
public class Program{
	public static void Main() {
		// zad 1
		// for (int i = 1; i < 31; i++){
            // Console.WriteLine(i);
	     //}
		 // zad 2
		/*for (int i = 1; i < 10; i++){
			if (i % 2 != 0){
				Console.WriteLine(Math.Pow(i, 2));
			}
		}
		*/
		// zad 3
		/*for (int i = 1000; i < 10000; i++){
			if (i % 379 == 0){
				Console.WriteLine(i);
			}
		}*/
		// zad 4
		/*for (int i = 10; i < 100; i++){
			if (i % 5 == 0 && i % 6 == 0 || i % 5 != 0 && i % 6 != 0 && i % 11 == 0){
				Console.WriteLine(i);
			}
		}*/
		// zad 5
		/*int n = int.Parse(Console.ReadLine());
		int sum = 0;
		for (int i = 1; i <= n; i++){
			sum += i;
		}
		Console.WriteLine(sum);*/
		
		// zad 6
		/*int k = int.Parse(Console.ReadLine());
		int sum = 0;
		for (int i = 1; i <= k*2; i += 2){
			sum += i;
		}
		Console.WriteLine(sum);*/
		
		//zad 7
		/*int k = int.Parse(Console.ReadLine());
		int sum = 0;
		for (int i = 1; i <= k*2+10; i += 2){
			sum += i;
		}
		Console.WriteLine(sum);*/
		
		// zad 8
	  /*double w = int.Parse(Console.ReadLine());
		int l = int.Parse(Console.ReadLine());
		double sum= w;
		double cap = 0;
		for (int i = 1; i <= l; i++)
		{
		cap = sum * 0.06;
    	sum += cap;
		}
		Console.WriteLine(Math.Round(sum, 2));*/
		// zad 9
	 /*int n = int.Parse(Console.ReadLine());
		int sum = 0;
		int a = 0;
		for (int i = 0; i <= n; i++){
    		a = i * 100 + 21;
			sum += a;
		}
		Console.WriteLine(sum);*/
		
		// zad 10
		 for (int i = 1; i < 1000; i++){
    	 	if ((i % 100 == Math.Sqrt(i)) || (i % 10 == Math.Sqrt(i))) {
				Console.WriteLine(i);
			}
		 }
        
	}
}