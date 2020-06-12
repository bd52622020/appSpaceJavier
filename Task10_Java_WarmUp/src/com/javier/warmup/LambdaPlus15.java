package com.javier.warmup;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class LambdaPlus15 {

//	Write a Python program to create a lambda function that adds 
//	15 to a given number passed in as an argument, also create a lambda 
//	function that multiplies argument a with argument b and print the result
	
	public static void main(String[] args) {
		
		
		Stream<Integer> examples1 = Stream.of(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4);
		List<Integer> res1 = examples1.map(i -> i+15).collect(Collectors.toList());
		System.out.println(res1);
		
		Stream<Integer> examples2 = Stream.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 4);
		Integer res2 = examples2.reduce(1, (acum, elem) -> acum * elem);
		System.out.println(res2);
		
	}
}
