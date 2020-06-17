package com.javier.warmup;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class T1_Dictionary_vehicles {

//	Given dictionary is consisted of vehicles and their weights in kilograms. 
//	Construct a list of the names of vehicles with weight below 5000 kilograms. 
//	In the same list comprehension make the key names all upper case. 
	
	public static void main(String[] args) {
		
		Map<String, Integer> vehicles = new HashMap<>();
		vehicles.put("car", 4000);
		vehicles.put("helicopter", 3000);
		vehicles.put("elephant", 5100);
		vehicles.put("plane", 10000);
		vehicles.put("quad", 200);
		
		List<String> vehiclesUpper5000 = vehicles.keySet().stream()
				.filter((key) -> vehicles.get(key) > 5000)
				.map((key) -> key.toUpperCase())
				.collect(Collectors.toList());
		
		System.out.println(vehiclesUpper5000);
		
		
	}
}
