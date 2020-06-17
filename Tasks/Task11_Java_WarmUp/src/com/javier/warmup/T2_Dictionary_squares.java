package com.javier.warmup;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class T2_Dictionary_squares {

	// Write a map function that returns the squares of the items in the list.
	
	public static void main(String[] args) {
		
		List<Integer> list = Arrays.asList(10, 20, 30, 40, 50, 600);
		List<Double> res = list.stream().map((x) -> Math.pow(x, 2)).collect(Collectors.toList());
		System.out.println(res);
	}
}
