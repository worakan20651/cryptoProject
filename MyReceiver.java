import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.util.Scanner;

public class MyReceiver {
    public static void main(String args) {
        String input = args;


        String binary = "";
        String plaintext = "";
        String cipher = "";

         try {
            // Create a FileReader object passing it the file path
            FileReader fileReader = new FileReader(input);
            
            // Wrap the FileReader in a BufferedReader for efficient reading
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            
            // Read the file line by line
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line); // Print each line
                cipher = line;
            }
            
            // Close the BufferedReader
            bufferedReader.close();
        } catch (IOException e) {
            // Handle any IO exceptions that may occur
            e.printStackTrace();
        }


        

        try {
            // Command to execute Python script (replace "python3" with "python" if needed)
            String Str = "python receiver.py \"" + cipher + "\"";
            // String Str = "ls -l";
            String[] command = Str.split(" ");
            System.out.println("Command " + String.join(" ", command));

            // Start the process
            Process process = Runtime.getRuntime().exec(command);

            // Read output from Python script
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            System.out.println("-----back to java----");
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
                plaintext = line;
            }

            // Wait for the process to finish
            process.waitFor();

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

        
        try {
            // Create a File object for the file
            File file = new File(input);
        
            // Get the file path
            String filePath = file.getAbsolutePath();
            System.out.println("File path: " + filePath);
        } catch (Exception e) {
            System.out.println("An error occurred while creating the file.");
            e.printStackTrace();
        }
    }
}

    
