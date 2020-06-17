package com.javier.warmup;

import java.time.LocalDate;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class T3_Dictionary_birthday {

//	Create a dictionary (in your file) of names and birthdays. When you run your 
//	program it should ask the user to enter a name, and return the birthday of 
//	that person back to them. The interaction should look something like this:
	
	public static void main(String[] args) {
		
		Map<String, LocalDate> birthdays = new HashMap<String, LocalDate>();
		birthdays.put("Sophie", LocalDate.of(2020, 7, 22));
		birthdays.put("Ramon", LocalDate.of(2002, 1, 21));
		birthdays.put("Tomas", LocalDate.of(2035, 2, 2));
		birthdays.put("Judini", LocalDate.of(1967, 5, 12));
		birthdays.put("James", LocalDate.of(1900, 3, 7));
		
		Scanner in = new Scanner(System.in);
		System.out.println("Write the date of your birthday (1967,5,12)...");
		System.out.println("First, write the year");
		int y = Integer.valueOf(in.nextLine());
		System.out.println("Second, write the month");
		int m = Integer.valueOf(in.nextLine());
		System.out.println("Third, write the day");
		int d = Integer.valueOf(in.nextLine());
		in.close();
		
		LocalDate inputDate = LocalDate.of(y, m, d);
		List<String> res = birthdays.entrySet().stream()
			.filter(entry -> inputDate.equals(entry.getValue()))
			.map(entry -> entry.getKey())
			.collect(Collectors.toList());
		
		System.out.println("The following people has the same birthday than you");
		System.out.println(res);
	}
}
