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
public class testcode {
    private static long bit_size;
    private static long prime;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        // String[] input = in.nextLine().split(" ");

        // // if (args.length < 2) {
        // // System.out.println("Please provide input and output files");
        // // System.exit(0);
        // // }

        // // File file = new File("1.png");
        // // File file = new File(input[0]);
        // // long bit = Long.parseLong(input[1]);
        // // String text = "";

        // // ...(file is initialised)...
        // bit_size = Long.parseLong(input[1]);
        // String filename = input[0];
        System.out.println(isPrime(3532802839l));
        System.out.println(3532802839l % 3313792338l);
        System.out.println(Long.MAX_VALUE);
        // long number = GenRandomNowithInverse((int)bit_size);

        // System.out.println(num);
        in.close();
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
            System.out.println("Found prime " + n);
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
            a = (a * a); // Change a to a^2 % n
        }
        return res % n;
    }

    private static boolean LehmanTest(long n) {
        // create instance of Random class
        Random rand = new Random();
        int t = 100;

        // generating a random base less than n

        // calculating exponent
        long e = (n - 1) / 2;
        System.out.println("Lehman's test");
        // iterate to check for different base values
        // for given number of tries 't'
        while (t > 0) {
            long a = rand.nextLong(n / 2);
            System.out.println("Test with a " + a);
            // System.out.println("a : " + a);
            // calculating final value using formula
            long result = (fastExpo(a, e, n));

            // System.out.println("check " + n + "with " + a);
            // if not equal, try for different base
            if (result != 1 || result != (n - 1)) {
                // System.out.println("prime? " + n + " with " + result);
                return false;
            }
            t--;

        }

        // return positive after attempting
        return true;
    }

    // random number by seed
    private static long xorShift(long seed) {
        seed ^= (seed << 21);
        seed ^= (seed >>> 35);
        seed ^= (seed << 4);
        return seed;
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
        while (GCD(prime, randomNumber) != 1) {
            random1 = RandomGenerator.of(String.valueOf(randomNumber));
            randomNumber = random1.nextLong();
        }
        return randomNumber;
    }
}