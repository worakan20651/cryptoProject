import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Random;

public class Generator {

    private static int bit_size;
    private static String fileName;

    // Generate prime number
    public static long GenPrime(int size, String file) {
        bit_size = size;
        fileName = file;
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
        long prime = 0l;
        for (long i = 0; i < binary.length(); i++) {
            if (binary.charAt((int) i) == '1') {
                tmp = binary.substring((int) i, (int) (i + size));
                break;
            }
        }

        // System.out.println(tmp);
        System.out.println("Number generate : " + tmp);
        prime = Long.parseLong(tmp, 2);
        System.out.println("Fisrt number generate : " + prime);
        // maximum range
        long k = (long) Math.pow(2, bit_size);

        System.out.println("k = " + k);
        // To return the value
        // of the number with set
        // bit at (31 - k)-th position
        // assuming 32 bits are used
        long bound = (long) Math.pow(2, bit_size) - 1;
        while ((isPrime(prime) == false) && prime < bound) {
            // System.out.println("Prime checking "+ prime);
            if (prime % 2 != 0) {
                prime += 2;
            } else {
                prime++;
            }
            // System.out.println("Check prime " + prime);
        }
        // System.out.println(tmp);

        return prime;
    }

    /**
     * Copy one file to another using low level byte streams, one byte at a time.
     * 
     * @author www.codejava.net
     */

    // read file and convert to binary
    private static String toBinary(byte[] bytes) {
        StringBuilder sb = new StringBuilder(bytes.length * Byte.SIZE);
        for (long i = 0; i < Byte.SIZE * bytes.length; i++)
            sb.append((bytes[(int) i / Byte.SIZE] << i % Byte.SIZE & 0x80) == 0 ? '0' : '1');
        return sb.toString();
    }

    // check primality using lehman's test with 100 number
    public static boolean isPrime(long n) {
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

    private static long fastExpo(long a, long b, long n) {
        long res = 1; // Initialize result

        while (b > 0) {
            // If b is odd, multiply result with a
            if ((b & 1) != 0)
                res = (res * a) % n;

            // b must be even now
            // Divide b by 2 and square a
            a = (a * a) % n;
            b = b / 2;
        }
        return res % n;
    }

    private static boolean LehmanTest(long n) {
        // create instance of Random class
        Random rand = new Random();
        int t = 0;

        // generating a random base less than n
        // calculating exponent
        long e = (n - 1) / 2;
        // System.out.println("Lehman's test");
        // iterate to check for different base values
        // for given number of tries 't'
        while (t < 100) {
            long a = rand.nextLong(n - 3) + 2;
            // System.out.println("Test with a " + a);
            // System.out.println("a : " + a);
            // calculating final value using formula
            // System.out.println("round " + t + " test with " + a);
            long result = (fastExpo(a, e, n));

            // System.out.println("check " + n + "with " + a);
            // if not equal, try for different base
            System.out.println("test " + a + " = " + result);
            if (result == 1 || result == (n - 1)) {
                // System.out.println("result " + a + " with " + result);
            } else {
                return false;
            }
            t++;
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

    public static long[] GenRandomNowithInverse(long n) {
        Random random = new Random();
        long e;
        do {
            e = Math.abs(random.nextLong() % (n - 1) + 1); // Generate a random number e in the range [1, n-1]
        } while (GCD(e, n) != 1); // Repeat until GCD(e, n) == 1
        // System.out.println("random number : " + arr[0]);
        return extendedGCD(e, n);
    }

    public static long[] extendedGCD(long a, long b) {
        long x = 0, y = 1, lastX = 1, lastY = 0, temp;
        long tempB = b, tempA = a;
        while (b != 0) {
            long quotient = a / b;
            long remainder = a % b;
            a = b;
            b = remainder;

            temp = x;
            x = lastX - quotient * x;
            lastX = temp;

            temp = y;
            y = lastY - quotient * y;
            lastY = temp;
        }
        return new long[]{lastX, lastY, tempA,tempB}; // Return [x, y, prime] where ax + by = gcd(a, b)
    }
}
