import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MySender {
    public static void main(String args) {

        String input = args;
        String binary = "";
        String cipher = "";
        String fileName = "";

        if (input.contains(".")) {
            binary = fileManage.readFileContent(input);
            fileName = "1_" + input;
        }

        else {
            String charsetName = "UTF-8";
            try {
                // Convert string to byte array
                byte[] byteArray = input.getBytes(charsetName);
                binary = fileManage.toBinary(byteArray);
                // System.out.println("Binary = " + binary);
                fileName = "1_cipher.txt";

            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
            }

        }

        String filedata = fileManage.writeBinary(binary, fileName);

        try {
            // Command to execute Python script (replace "python3" with "python" if needed)
            String Str = "python sender.py "+ filedata + " " + fileName;
            // String Str = "ls -l";
            String[] command = Str.split(" ");

            System.out.println("Command " + String.join(" ", command));

            // Start the process
            Process process = Runtime.getRuntime().exec(command);

            // Read output from Python script
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            // System.out.println("-----back to java----");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
                cipher = line;
            }
            // System.out.println("cipher in java " + cipher);

            // Wait for the process to finish
            process.waitFor();

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

    }

    
}
