import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class elgaSystem {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String filename = "";
        char mode;

        do {
            System.out.println("Type the MODE you want to use");
            System.out.println("G for Generate your key pair");
            System.out.println("S for Encrypt you message or file");
            System.out.println("R for Decrypt you cipher message or file");
            System.out.println("X to exit this program");
            mode = in.next().charAt(0);
            switch (mode) {
                case 'G':
                    System.out.println("This is Generator mode\nInput your maximum bit to generate = ");
                    int bits = in.nextInt();
                    try {
                        String key = "";
                        String str = "python ElgamalGenerator.py  \"" + bits + "\"";

                        // String Str = "ls -l";
                        String[] command = str.split(" ");
                        System.out.println("Command " + String.join(" ", command));

                        // Start the process
                        Process process = Runtime.getRuntime().exec(command);

                        // Read output from Python script
                        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                        String line;
                        System.out.println("-----back to java----");
                        while ((line = reader.readLine()) != null) {
                            System.out.println(line);
                            key = line;
                        }

                        // Wait for the process to finish
                        process.waitFor();

                        fileManage.writeFile(key, "publicKeyDirectory.txt");

                    } catch (Exception e) {
                        System.err.println("Something went wrong with input");
                    }
                    break;

                case 'S':
                    System.out.print("Enter file/message you want to send : ");
                    filename = in.nextLine();
                    MySender.main(filename);
                    break;

                case 'R':
                    System.out.print("Enter file/message you want to send : ");
                    filename = in.nextLine();
                    MyReceiver.main(filename);
                    break;

                default:
                    System.out.println("-------Thank you-------");
                    break;
            }
        } while (mode == 'G' || mode == 'S' || mode == 'R' || mode == 'g' || mode == 's' || mode == 'r');

        in.close();
    }
}
