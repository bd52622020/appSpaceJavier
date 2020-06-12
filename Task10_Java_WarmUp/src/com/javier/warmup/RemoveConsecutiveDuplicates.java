package com.javier.warmup;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class RemoveConsecutiveDuplicates {
	
			
	public static void main(String[] args) {
		
		List<Integer> duplicates = Stream.of(0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4).collect(Collectors.toList());
		List<Integer> res = new ArrayList<Integer>();
		res.add(duplicates.get(0));
		
		for(int i=1; i < duplicates.size()-1; i++) {
			Integer actual = duplicates.get(i);
			Integer prev = duplicates.get(i-1);
			if (prev != actual) {
				res.add(actual);
			}
		}
		System.out.println(res);
	}
}
