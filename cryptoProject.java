import java.util.Scanner;


public class cryptoProject {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String[] input = in.nextLine().split(" ");

        // // if (args.length < 2) {
        // // System.out.println("Please provide input and output files");
        // // System.exit(0);
        // // }

        // // File file = new File("1.png");
        // // File file = new File(input[0]);
        // // long bit = Long.parseLong(input[1]);
        // // String text = "";

        // ...(file is initialised)...
        int bit_size = Integer.parseInt(input[1]);
        String filename = input[0];
        long prime = Generator.GenPrime(bit_size, filename);
        System.out.println("prime is " + prime);
        long[] arr = Generator.GenRandomNowithInverse(prime);
        System.out.println("inverse1 : "+ arr[0] + " | inverse2 : "+ arr[1] + " | randomNum : "+ arr[2]+ " | Prime : "+arr[3]);
        // long number = GenRandomNowithInverse((int)bit_size);
        // System.out.println(Generator.isPrime(2147483647));

        // System.out.println(isPrime(3532802839l));
        // System.out.println(num);
        in.close();
    }
}