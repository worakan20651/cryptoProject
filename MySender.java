import java.io.BufferedReader;
import java.io.File;
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
        int[][] block_cipher = mappingStringToIntArr(cipher);
        fileManage.writeFile(fileName, block_cipher);

    }

    public static int[][] mappingStringToIntArr(String str){
        // Regular expression to match integers enclosed in square brackets
        Pattern pattern = Pattern.compile("\\[(\\d+),\\s*(\\d+)\\]");
        Matcher matcher = pattern.matcher(str);

        int[][] intArray = new int[2][2]; // Initialize a 2x2 array to hold the integers

        int row = 0; // Initialize row index
        while (matcher.find()) {
            // Extract and parse the integers
            int firstInt = Integer.parseInt(matcher.group(1));
            int secondInt = Integer.parseInt(matcher.group(2));

            // Store the integers in the array
            intArray[row][0] = firstInt;
            intArray[row][1] = secondInt;

            // Move to the next row
            row++;
        }
        return intArray;
    } 
}
