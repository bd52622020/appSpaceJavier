package com.javier.warmup;

import java.security.SecureRandom;
import java.util.Random;
import java.util.Scanner;

public class T4_Password_generator {

//	Write a password generator in Python. Be creative with how you generate passwords - strong 
//	passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The 
//	passwords should be random, generating a new password every time the user asks for a new 
//	password. Include your code in a main method
	
	public String createPassword(int n) {
		final String CHARS = "!@#$%,./?0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
	    
	    Random random = new SecureRandom();
	    StringBuilder sb = new StringBuilder();
	    
	    for(int i=0; i < n; i++) {
	    	int randomChar = random.nextInt(CHARS.length());
	    	sb.append(CHARS.charAt(randomChar));
	    }
	 
	    return sb.toString();
	}
	
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		System.out.println("Write the length of your password:");
		int n = Integer.valueOf(in.nextLine());
		in.close();
		
		T4_Password_generator generator = new T4_Password_generator();
		String password = generator.createPassword(n);
		Boolean isPasswordSafe = false;
		
	    while (isPasswordSafe != true) {
	    	password = generator.createPassword(n); 
	    	isPasswordSafe = password.matches(".*[A-Z].*") && password.matches(".*[!@#$%,./?].*") && password.matches(".*[0-9].*") && password.matches(".*[a-z].*");
	    }
	    
	    System.out.println("Password: " + password);
	}
}
