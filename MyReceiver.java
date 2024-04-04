import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class MyReceiver {
    public static void main(String args) {
        String input = args;
        // System.out.println("test input "+input);
        String binary = "";

        try {
            // Command to execute Python script (replace "python3" with "python" if needed)
            String Str = "python receiver.py " + input;
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
            }

            process.waitFor();

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }

        // try {
            // Create a File object for the file
            // File file = new File(input);

        //     // Get the file path
        //     String filePath = file.getAbsolutePath();
        //     System.out.println("File path: " + filePath);
        // } catch (Exception e) {
        //     System.out.println("An error occurred while creating the file.");
        //     e.printStackTrace();
        // }
    }

}
