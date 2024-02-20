import java.io.*;
import java.nio.file.Files;
import java.util.Random;
import java.util.Scanner;
import java.util.random.RandomGenerator;

/**
 * Copy one file to another using low level byte streams, one byte at a time.
 * 
 * @author www.codejava.net
 */
public class cryptoProject {
    private static long bit_size;
    private static long prime;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] input = in.nextLine().split(" ");

        // if (args.length < 2) {
        // System.out.println("Please provide input and output files");
        // System.exit(0);
        // }

        // File file = new File("1.png");
        // File file = new File(input[0]);
        // long bit = Long.parseLong(input[1]);
        // String text = "";

        // ...(file is initialised)...
        bit_size = Long.parseLong(input[1]);
        String filename = input[0];
        prime = GenPrime(bit_size, filename);
        System.out.println("prime is "+prime);
        // long number = GenRandomNowithInverse((int)bit_size);

        // System.out.println(num);
        in.close();
    }

    // Generate prime number
    public static long GenPrime(long size, String fileName) {
        byte[] fileContent;
        String binary = "";
        try {
            fileContent = Files.readAllBytes(new File(fileName).toPath());
            binary = toBinary(fileContent);
        }

        catch (IOException e) {
            System.err.println("File not found");
        } catch (NullPointerException e) {
            System.err.println("incomplete read file");
        }

        String tmp = "";
        long prime = 0;
        for (long i = 0; i < binary.length(); i++) {
            if (binary.charAt((int) i) == '1') {
                tmp = binary.substring((int) i, (int) (i + size));
                break;
            }
        }
        // System.out.println(tmp);
        System.out.println("Number generate : "+tmp);
        prime = Long.parseLong(tmp, 2);
        System.out.println("Fisrt number generate : "+ prime);
        //maximum range
        long k = (long)Math.pow(2,bit_size);
 
        System.out.println("k = "+k);
        // To return the value
        // of the number with set
        // bit at (31 - k)-th position
        // assuming 32 bits are used
        while ((isPrime(prime) == false) && prime < Math.pow(2,bit_size) - 1) {
            // System.out.println("Prime checking "+ prime);
            if (prime % 2 != 0) {
                prime += 2;
            } else {
                prime++;
            }
            System.out.println("Check prime "+ prime);
        }
        // System.out.println(tmp);

        return prime;
    }

    // read file and convert to binary
    private static String toBinary(byte[] bytes) {
        StringBuilder sb = new StringBuilder(bytes.length * Byte.SIZE);
        for (long i = 0; i < Byte.SIZE * bytes.length; i++)
            sb.append((bytes[(int) i / Byte.SIZE] << i % Byte.SIZE & 0x80) == 0 ? '0' : '1');
        return sb.toString();
    }

    // check primality using lehman's test with 100 number
    private static boolean isPrime(long n) {
        // กรณีพิเศษเมื่อ n เป็นจำนวนเฉพาะที่มีค่าเล็ก
        if (n == 2 || n == 3 || n == 5)
            return true;
        if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0)
            return false;

        // ใช้ Lehman Test ตรวจสอบว่า n เป็นจำนวนเฉพาะหรือไม่   
        if (LehmanTest(n)) {
            return true;
        }
        return false;
    }

    private static long GCD(long a, long n) {
        long x = 0, y = 0;
        // Base Case
        if (a == 0) {
            x = 0;
            y = 1;
            return n;
        }

        // To store results of recursive call
        long gcd = GCD(n % a, a);
        long x1 = x;
        long y1 = y;

        // Update x and y using results of recursive
        // call
        long tmp = n / a;
        x = y1 - tmp * x1;
        y = x1;

        return gcd;
    }

    private static long FindInverse(long a, long p) {
        long X;
        for (X = 1; X < p; X++) {
            if (((a % p) * (X % p)) % p == 1)
                return X;
        }
        return 1;
    }

    private static long fastExpo(long a, long b, long n) {
        long res = 1; // Initialize result

        while (b > 0) {
            // If b is odd, multiply result with a
            if ((b & 1) != 0)
                res = (res * a) % n;
    
            // b must be even now
            // Divide b by 2 and square a
            b = b >> 1; // b = b/2
            a = (a * a) % n; // Change a to a^2 % n
        }
        return res % n;
    }

    // private static boolean LehmanTest(long a, long n) {
    // long x = fastExpo(a, (n - 1) / 2, n);
    // long y = GCD(a, n);
    // if (y != 1)
    // return false;
    // long result = (x * y) % n;
    // if (result == n - 1)
    // return true;
    // return false;
    // }
    private static boolean LehmanTest(long n) {
        // create instance of Random class
        Random rand = new Random();
        int t = 100;

        // generating a random base less than n
        long a = rand.nextLong(n - 3) + 2;

        // calculating exponent
        long e = (n - 1) / 2;

        // iterate to check for different base values
        // for given number of tries 't'
        while (t > 0) {
            
            System.out.println("a : "+ a);
            // calculating final value using formula
            long result = (fastExpo(a, e, n));

            // System.out.println("check " + n + "with " + a);
            // if not equal, try for different base
            if (result == 1 || result == (n - 1)) {
                System.out.println("prime? " + n +" with " + result);
                a = rand.nextLong(n - 3) + 2;
                t -= 1;
            }

            // else return negative
            else
                return false;

        }

        // return positive after attempting
        return true;
    }

    // user-defined method that contains the logic to find the square root
    public static long squareRoot(long num) {
        // temporary variable
        double t;
        double sqrtroot = num / 2;
        do {
            t = sqrtroot;
            sqrtroot = (t + (num / t)) / 2;
        } while ((t - sqrtroot) != 0);
        return (long) sqrtroot;
    }

    public static long GenRandomNowithInverse(int n) {
        RandomGenerator random1 = RandomGenerator.of(String.valueOf(System.currentTimeMillis()));
        long randomNumber = random1.nextLong();
        while(GCD(prime, randomNumber) != 1){
            random1 = RandomGenerator.of(String.valueOf(randomNumber));
            randomNumber = random1.nextLong();
        }
        return randomNumber;
    }
}