import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;

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
                System.out.println("Binary = " + binary);
                fileName = "1_cipher.txt";

            } catch (UnsupportedEncodingException e) {
                e.printStackTrace();
            }

        }

        try {
            // Command to execute Python script (replace "python3" with "python" if needed)
            String Str = "python sender.py \"" + binary + "\"";
            // String Str = "ls -l";
            String[] command = Str.split(" ");

            // System.out.println("Command " + String.join(" ", command));

            // Start the process
            Process process = Runtime.getRuntime().exec(command);

            // Read output from Python script
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            System.out.println("-----back to java----");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
                cipher = line;
            }
            System.out.println("cipher in java " + cipher);

            // Wait for the process to finish
            process.waitFor();

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

        try {
            // Create a File object
            File file = new File(fileName);

            // Create the file if it doesn't exist
            if (file.createNewFile()) {
                System.out.println("File created successfully.");
            } else {
                System.out.println("File already exists.");
            }

            // Get the file path
            String filePath = file.getAbsolutePath();
            System.out.println("File path: " + filePath);
        } catch (IOException e) {
            System.out.println("An error occurred while creating the file.");
            e.printStackTrace();
        }

        fileManage.writeFile(fileName, cipher);

    }
}
