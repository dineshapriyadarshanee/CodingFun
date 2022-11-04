import java.io.*;
import  java.lang.Math;

public class HelloWorld
{

     public static void main(String []args) throws IOException
     {
        System.out.println("Welcome to the simple math helper.");
        System.out.println("What would you like to calculate?\n");
        System.out.println("\t 1. Sqrt\n" + "\t 2. Log \n" + "\t 3. Factorial \n");
        
        // Read user input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int i=0;
        
        // Handle the exceptions for invalid inputs
        try
        {
            i = Integer.parseInt(s);
            if(i<0 || i>3)
            {
                System.out.println("Please enter a valid value.");
            }
        }
        catch(Exception ex)
        {
                System.out.println("Please enter a valid value.");
        }
        calculateResult(i);
        }
        
        public static void calculateResult(int i) throws IOException{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            switch(i)
            {
                case 1:
                    System.out.println("Enter the number to sqrt:");
                    String s = br.readLine();
                    System.out.println(Math.sqrt(Double.parseDouble(s)));
                    
                case 2:
                    System.out.println("Enter the number to log:");
                    String l = br.readLine();
                    System.out.println(Math.log(Double.parseDouble(l)));
                    
                case 3:
                    System.out.println("Enter the number to Factorial:");
                    String f = br.readLine();
                    findFactorial(Integer.parseInt(f));
                    
            }
        }
            
            public static void findFactorial(int f)
            {
                int result = f;
                for(int i = f-1; i>0 ; i--)
                {
                    result = result * i;
                }
                System.out.println(result);
            }
        
}
