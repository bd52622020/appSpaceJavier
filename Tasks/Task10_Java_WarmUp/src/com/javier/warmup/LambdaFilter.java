package com.javier.warmup;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LambdaFilter {

	//Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
	
	
	public static void main(String[] args) {
		
		List<Integer> numbers = Arrays.asList(167,286,336,38,26,600);
		List<Integer> res = numbers.stream().filter(i -> i%19 == 167 || i%13 == 0).collect(Collectors.toList());
		System.out.println(res);
	}
}
