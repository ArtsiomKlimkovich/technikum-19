using System;
using System.Collections.Generic;	
public class Program{
	public static void Main(){
		Category menu = new Category("Menu Restauracji La Dolce Vita");
		
		Category Zupy = new Category("Zupy");
		Category Glowne = new Category("Dania Glowne");
		Category Desery = new Category("Desery");
		
		Dish zupa1 = new Dish("Zupa Pomidorowa", 5.99);
		Dish zupa2 = new Dish("Zupa Krem z Brokułów", 6.49);
		Zupy.add(zupa1);
		Zupy.add(zupa2);
		
		Dish glowne1 = new Dish("Spaghetti Bolognese", 12.99);
		Dish glowne2 = new Dish("Filet z Kurczaka z Grill", 15.99);
		Glowne.add(glowne1);
		Glowne.add(glowne2);
		
		Dish desery1 = new Dish("Tiramisu", 7.49);
		Dish desery2 = new Dish("Sernik Waniliowy", 6.99);
		Desery.add(desery1);
		Desery.add(desery2);
		
		menu.add(Zupy);
		menu.add(Glowne);
		menu.add(Desery);
		
		menu.wyswietl();
		
	}
}

public abstract class Kind{
	public string name;
	public abstract void wyswietl();
}

public class Dish : Kind{
	public double price;
	public Dish(string name, double price){
		this.name = name;
		this.price = price;
	}
	
	public override void wyswietl(){
		Console.Write("  ");
		Console.WriteLine(name + " - " + "$" + price);
	}
}

public class Category : Kind{
	List<Kind> kinds = new List<Kind>();
	public Category(string name){
		this.name = name;
	}
	public void add(Kind kind){
		kinds.Add(kind);
	}
	public override void wyswietl(){
		Console.WriteLine(name);
		foreach (var item in kinds){
			Console.Write("-- ");
			item.wyswietl();
		}
	}
}
